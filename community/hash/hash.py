import hashlib
import logging

from arcapix.search.metadata.plugins.base import Plugin, PluginStatus
from arcapix.search.metadata.helpers import Metadata

logger = logging.getLogger(__name__)


class FileHashPlugin(Plugin):
    """Plugin that calculates the hash of a file.
    
    Can be used to identify duplicates.
    """
    
    def namespace(self):
        return 'core'
    
    def schema(self):
        return [{
            "name": "hash",
            "prompt": "MD5 hash of the file contents",
            "value": {
                "datatype": "String"
            }
        }]

    def process(self, id_, file_, fileinfo=None):
        try:
            
            blocksize = (fileinfo or {}).get('gpfs', {}).get('blocksize', 65536)
            data = {'hash': md5sum(file_, blocksize)}
            
            if Metadata(id_, self).update(data):
                return PluginStatus.SUCCESS
            
            return PluginStatus.ERRORED
        
        except:
            logger.exception("Error while processing %r (%s)", file_, id_)
            return PluginStatus.FATAL


def md5sum(filename, blocksize=65536):
    """Method to calculate md5sum of a file."""
    hash = hashlib.md5()
    try:
        with open(filename, "rb") as f:
            for block in iter(lambda: f.read(blocksize), b""):
                hash.update(block)
    except:
        logger.warn("Couldn't md5 hash %r", filename)
        # exclude any files that can't be read
        return None
    return hash.hexdigest()

