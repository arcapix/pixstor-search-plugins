import logging
import os
import numpy as np
from argparse import ArgumentParser
from PIL import Image

# we already use this for video thumbnail generation
from storyboard.storyboard import StoryBoard

from arcapix.search.metadata.helpers import Proxy
from arcapix.search.metadata.plugins.base import ProxyPlugin, PluginStatus

from arcapix.config import config

logger = logging.getLogger('arcapix.search.metadata.plugins.ext.videobarcode')


class VideoBarcodeProxy(ProxyPlugin):
    """Proxy to generate a 'barcode' visualisation of a video.

    Inspired by:

    http://www.pyimagesearch.com/2017/01/16/generating-movie-barcodes-with-opencv-and-python/
    """

    def namespace(self):
        return 'video'

    def handles(self, ext=None, mimetype=None):
        return mimetype and mimetype.startswith('video/')

    def async(self):
        return True

    def schema(self):
        return [{
            "name": "barcode",
            "prompt": "Video barcode visualisation",
            "value": {
                "datatype": "Proxy"
            }
        }]

    def process_async(self, id_, source_path, thumbnail_size):
        """Make the proxy and add it to the proxy store/db"""
        proxy_filename = self.generate_temp_filename(suffix='.png')

        generate_barcode(source_path, proxy_filename, thumbnail_size, max_frames=100, force_size=True)

        try:
            Proxy(id_, self).ingest(proxy_filename, 'barcode', 'barcode.png', 'image/png')
        finally:
            if os.path.exists(proxy_filename):
                os.remove(proxy_filename)

    def process(self, id_, file_, fileinfo=None):
        """Generate a downsized version of the video for previewing.

        Proxygen is performed async
        """
        try:
            self._submit(self.process_async, args=[id_, file_, config['arcapix.search.proxies.preview.size']])
            return PluginStatus.INPROGRESS

        except Exception as e:
            self.logger.error(
                "An exception was raised while processing '%s' (%s) with %s - %s: %s",
                file_, id_, self.__class__.__name__, e.__class__.__name__, e)
            self.logger.debug("Traceback while processing %r (%s)", file_, id_, exc_info=True)
            return PluginStatus.FATAL


def get_target_frame_count(sb, target_width, max_frames=None, min_bar_width=1):
    """Calculate how many frames of the video should be extracted.

    Also calculates the width for each bar in the bar code.

    Together the frame count and bar width determine the
    actual width of the generate barcode, which may differ
    from the specified target width.

    :returns: frame count and bar width
    """
    frame_count = sb.video.duration * sb.video.frame_rate - 1

    # fewer frames than image width - make bar wider
    if frame_count * min_bar_width < target_width:
        bar_width = target_width // frame_count
        frames = frame_count

    # more frames than width, trim frame count
    else:
        frames = target_width // min_bar_width
        bar_width = min_bar_width

    # if required, limit frame count and expand bar to fit
    if max_frames and frames > max_frames:
        frames = max_frames
        bar_width = target_width // max_frames

    return int(frames), int(round(bar_width))


def get_frames(source, size, max_frames=None, min_bar_width=1):
    """Get video frames to generate barcode from.

    :param string source: path to source video
    :param tuple size: the desired output image size (width, height)
    :param int max_frames: limit the number of frames extracted.
        Will make extraction faster for longer videos.
    :param int min_bar_width: minimum width per bar of the generated barcode.

    :returns: list of PIL Image objects
    """
    s = StoryBoard(str(source))  # storyboard doesn't like unicode

    frame_count, bar_width = get_target_frame_count(
        s, size[0], max_frames, min_bar_width)

    logger.info("Generating %d frames, with bar width %d", frame_count, bar_width)
    logger.debug("Resulting image width: %d", frame_count * bar_width)

    try:
        s.gen_frames(frame_count)
    except OSError:  # sometimes the frame count goes out of index
        logger.warning("Error from ffmpeg while generating frames")

    logger.info("Generated %d frames", len(s.frames))

    return [f.image for f in s.frames], bar_width


def calculate_average_colors(frames):
    """Calculate average colour for each of a list of frames.

    :param list frames: list of video frames

    Each frame should be a PIL Image or numpy array
    where the 3rd axis is (R, G, B)

    :returns: list of average colours for each frame
    """
    logger.info("Calculating averages...")

    avgs = [np.mean(frame, axis=(0, 1)) for frame in frames]
    avgs = np.array(avgs, dtype="int")

    return avgs


def generate_barcode_from_colors(colors, bar_size):
    """Generate a barcode visualisation image from a list of colours.

    :param list colors: list of colors in the form of (R, G, B)
    :param tuple bar_size: size of a single bar as (width, height)

    :returns: generated barcode
    :rtype: PIL.Image
    """
    width, height = bar_size

    logger.info("Generating barcode image...")

    # allocate memory for the barcode visualization
    # note: reversed (width, height)
    barcode = np.zeros((height, len(colors) * width, 3), dtype="uint8")

    for i, color in enumerate(colors):
        for x in xrange(i * width, (i + 1) * width):
            for y in xrange(0, height):
                barcode[y][x] = color

    return Image.fromarray(barcode)


def generate_barcode(source, target, size, max_frames=None, min_bar_width=1, force_size=False):
    """Generate a 'barcode' visualisation image from a video."""
    min_bar_width = max(min_bar_width, 1)  # sanity check

    frames, bar_width = get_frames(source, size, max_frames, min_bar_width)

    avgs = calculate_average_colors(frames)

    # maintain aspect ratio
    bar_height = int((size[1] * bar_width * len(frames)) / float(size[0]))
    logger.debug("Generating barcode image with size: (%d, %d)", bar_width * len(frames), bar_height)

    barcode = generate_barcode_from_colors(avgs, (bar_width, bar_height))

    if force_size and tuple(barcode.size) != tuple(size):
        logger.info("Resizing from %r to %r", barcode.size, size)
        # use nearest neigbour to maintain crispness
        barcode = barcode.resize(size, Image.NEAREST)

    logger.info("Saving barcode image to %r", target)
    barcode.save(target)


if __name__ == '__main__':
    """Run barcode generation as a command line script."""
    parser = ArgumentParser()

    parser.add_argument('source', help='Source video file')
    parser.add_argument('target', help='Target image file to save to')

    parser.add_argument('-W', '--width', type=int, required=True, help="Target image width")
    parser.add_argument('-H', '--height', type=int, required=True, help="Target image width")

    parser.add_argument(
        '--max-frames', type=int,
        help="Limit the number of frames that are extracted"
    )
    parser.add_argument(
        '--min-bar-width', type=int, default=1,
        help="Minimum width per bar of barcode (default = 1 pixel)"
    )
    parser.add_argument(
        '--force-size', action='store_true',
        help=("Force the resulting image to match the specified size. "
              "Without this flag the resulting image may be slightly "
              "bigger or smaller than the size specified"
              ))

    args = parser.parse_args()

    generate_barcode(args.source, args.target, (args.width, args.height),
                     args.max_frames, args.min_bar_width, args.force_size)
