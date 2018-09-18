import logging
from subprocess import check_output

import numpy as np
import matplotlib

# enable for 'headless' image generation
# this must appear before the pyplot import
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from scipy import signal

from arcapix.search.metadata.plugins.thumbnails import _Thumbnail

logger = logging.getLogger(__name__)


class AudioThumbnail(_Thumbnail):
    """General purpose thumbnail generator for audio files."""

    def namespace(self):
        return 'audio'

    def handles(self, ext=None, mimetype=None):
        # Note - this plugin will _try_ to handle all audio formats
        # but it may not actually work for all possible formats
        return mimetype and mimetype.startswith('audio/')

    def _make_proxy(self, source_path, thumbnail_size):
        """Make a spectrogram thumbnail image.

        Makes a thumbnail image out of a section
        of the audio file's spectrogram.
        """
        rate = 21500
        M = 1024

        # convert the audio file into something
        # that can be processed as a numpy array
        FFMPEG_BIN = "/usr/bin/ffmpeg"

        command = [
            FFMPEG_BIN,
            '-ss', '5',  # skip to 5s in
            '-t', '5',  # only read 5s
            '-i', source_path,  # input
            '-f', 's16le',
            '-acodec', 'pcm_s16le',
            '-ar', str(rate),  # sample rate
            '-ac', '1',  # mono
            '-loglevel', 'quiet',
            '-']  # pipe converted to stdout

        raw_audio = check_output(command)

        audio = np.fromstring(raw_audio, dtype="int16")
        audio = audio.reshape((len(audio) / 2, 2))
        audio = np.mean(audio, axis=1)

        # build the spectrogram
        freqs, times, Sx = signal.spectrogram(
            audio, fs=rate, window='hanning',
            nperseg=1024, noverlap=M - 100,
            detrend=False, scaling='spectrum')

        # format plot to exclude axes, borders, etc.
        fig = plt.figure()
        fig.set_size_inches(
            thumbnail_size[0] / 80.,
            thumbnail_size[1] / 80.
        )
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)

        # draw plot
        plt.pcolormesh(times, freqs, 10 * np.log10(Sx), cmap='viridis')

        proxy_filename = self.generate_temp_filename(suffix='.png')

        # save image file
        plt.savefig(proxy_filename, dpi=80)

        return proxy_filename
