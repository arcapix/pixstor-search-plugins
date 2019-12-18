from bisect import bisect
import numpy as np

from arcapix.search.metadata.plugins.base import Plugin, PluginStatus
from arcapix.search.metadata.helpers import Metadata
from arcapix.search.metadata.utils import load_image

BOUNDS = [0, 15, 33, 45, 59, 82, 109]


class ColourfulnessPlugin(Plugin):

    def namespace(self):
        return 'image'

    def handles(self, ext=None, mimetype=None):
        return mimetype and mimetype.startswith('image/')

    def schema(self):
        return [{
            "name": "colourfulness",
            "prompt": "Rating of how colourful the image is (0-6)",
            "value": {
                "datatype": "Integer"
            }
        }]

    def _extract(self, filename):
        value = image_colourfulness(filename)

        return {'colourfulness': bisect(BOUNDS, value) - 1}

    def process(self, id_, file_, fileinfo=None):
        try:
            data = self._extract(file_)

            if Metadata(id_, self).update(data):
                return PluginStatus.SUCCESS

            return PluginStatus.ERRORED

        except Exception as e:
            self.logger.error(
                "An exception was raised while processing '%s' (%s) with %s - %s: %s",
                file_, id_, self.__class__.__name__, e.__class__.__name__, e)
            self.logger.debug("Traceback while processing %r (%s)", file_, id_, exc_info=True)
            return PluginStatus.FATAL


def image_colourfulness(filename):
    """Calculate a 'colourfulness' metric for an image.

    Adapted from http://www.pyimagesearch.com/2017/06/05/computing-image-colorfulness-with-opencv-and-python/
    """
    # load image and resize
    image = load_image(filename)
    image.shrink((250, 250))
    ar = image.to_numpy()

    # split the image into its respective RGB components
    (R, G, B) = [ar[:, :, i] for i in range(3)]

    # compute rg = R - G
    rg = np.absolute(R - G)

    # compute yb = 0.5 * (R + G) - B
    yb = np.absolute(0.5 * (R + G) - B)

    # compute the mean and standard deviation of both `rg` and `yb`
    (rbMean, rbStd) = (np.mean(rg), np.std(rg))
    (ybMean, ybStd) = (np.mean(yb), np.std(yb))

    # combine the mean and standard deviations
    stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
    meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))

    # derive the "colorfulness" metric and return it
    return stdRoot + (0.3 * meanRoot)
