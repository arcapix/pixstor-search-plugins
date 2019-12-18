import hashlib
import logging

from arcapix.search.metadata.plugins.base import Plugin, PluginStatus
from arcapix.search.metadata.helpers import Metadata

logger = logging.getLogger('arcapix.search.metadata.plugins.ext.md5hash')


class Md5HashPlugin(Plugin):
    """Plugin that calculates the md5 hash of a file.

    Can be used to identify duplicates.
    """

    def namespace(self):
        return 'core'

    def handles(self, ext=None, mimetype=None):
        return mimetype != 'inode/directory'

    def schema(self):
        return [{"hash": [{
            "name": "md5",
            "prompt": "MD5 hash of the file contents",
            "value": {
                "datatype": "String"
            }
        }]}]

    def process(self, id_, file_, fileinfo=None):
        try:

            blocksize = (fileinfo or {}).get('gpfs', {}).get('blocksize', 65536)
            data = {'hash': {'md5': md5sum(file_, blocksize)}}

            if Metadata(id_, self).update(data):
                return PluginStatus.SUCCESS

            return PluginStatus.ERRORED

        except Exception as e:
            self.logger.error(
                "An exception was raised while processing '%s' (%s) with %s - %s: %s",
                file_, id_, self.__class__.__name__, e.__class__.__name__, e)
            self.logger.debug("Traceback while processing %r (%s)", file_, id_, exc_info=True)
            return PluginStatus.FATAL


def md5sum(filename, blocksize=65536):
    """Method to calculate md5sum of a file."""
    hash = hashlib.md5()
    try:
        with open(filename, "rb") as f:
            for block in iter(lambda: f.read(blocksize), b""):
                hash.update(block)
    except Exception:
        logger.warning("Couldn't md5 hash %r", filename)
        # exclude any files that can't be read
        return None
    return hash.hexdigest()
