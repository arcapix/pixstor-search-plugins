from arcapix.search.metadata.plugins.base import Plugin, PluginStatus
from arcapix.search.metadata.helpers import Metadata
from arcapix.search.metadata.utils import load_image


class AllBlackImagePlugin(Plugin):
    """Identify images that are completely black."""

    def namespace(self):
        return 'image'

    def handles(self, ext=None, mimetype=None):
        return mimetype and mimetype.startswith('image/')

    def schema(self):
        return [{
            "name": "all_black",
            "prompt": "Specifies whether the image is all black",
            "value": {
                "datatype": "Boolean"
            }
        }]

    def _extract(self, filename):
        im = load_image(filename)
        ar = im.to_numpy().astype(int)

        # if the image is all black, all its values will be 0
        return {'all_black': not sum(sum(sum(ar)))}

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
