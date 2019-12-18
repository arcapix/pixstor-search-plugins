from imagehash import phash

from arcapix.search.metadata.plugins.base import Plugin, PluginStatus
from arcapix.search.metadata.helpers import Metadata
from arcapix.search.metadata.image import PillowImage
from arcapix.search.metadata.utils import load_image


class ImageHashPlugin(Plugin):
    """Plugin that calculates the perceptual hash of an image file.

    Can be used to identify duplicates.

    Unlike md5 hash, this hash is based on the visual content of the image.

    For comparing the exact hash, matches will include exact duplicates
    as well as resized versions of an image. It also has a certain tolerance
    for things like gamma levels, artifacts and noise.

    Ideally, hashes would be compared by Hamming distance to find
    similar images - however Elasticsearch does support such functionality.
    """

    def namespace(self):
        return 'image'

    def handles(self, ext=None, mimetype=None):
        return mimetype and mimetype.startswith('image/')

    def schema(self):
        return [{
            "name": "phash",
            "prompt": "Perceptual hash of the image",
            "value": {
                "datatype": "String"
            }
        }]

    def process(self, id_, file_, fileinfo=None):
        try:
            # phash requires a PIL.Image
            # load_image may return a WandImage, so we need to convert
            im = load_image(file_)

            data = {'phash': str(phash(im.image))}

            if Metadata(id_, self).update(data):
                return PluginStatus.SUCCESS

            return PluginStatus.ERRORED

        except Exception as e:
            self.logger.error(
                "An exception was raised while processing '%s' (%s) with %s - %s: %s",
                file_, id_, self.__class__.__name__, e.__class__.__name__, e)
            self.logger.debug("Traceback while processing %r (%s)", file_, id_, exc_info=True)
            return PluginStatus.FATAL
