from arcapix.search.metadata.plugins.base import Plugin, PluginStatus
from arcapix.search.metadata.helpers import Metadata
from arcapix.search.metadata.utils import get_ffprobe_data


class VideoCodecPlugin(Plugin):

    def namespace(self):
        return 'video'

    def handles(self, ext=None, mimetype=None):
        return mimetype and mimetype.startswith("video/")

    def schema(self):
        return [
            {"codec": [
                {
                    "name": "audio",
                    "prompt": "Audio codec name",
                    "value": {
                        "datatype": "String"
                    }
                },
                {
                    "name": "video",
                    "prompt": "Video codec name",
                    "value": {
                        "datatype": "String"
                    }
                }
            ]}]

    def _extract(self, filename):
        data = get_ffprobe_data(filename, ['-show_streams'])

        result = {}

        for stream in data.get('streams', []):
            if stream['codec_type'] in ('audio', 'video'):
                result[stream['codec_type']] = stream['codec_name']

        if result:
            return {'codec': result}

        return None

    def process(self, id_, file_, fileinfo=None):
        try:
            data = self._extract(file_)

            if not data:
                # didn't find any metadata
                return PluginStatus.SKIPPED

            if Metadata(id_, self).update(data):
                return PluginStatus.SUCCESS

            # posting to datastore failed
            return PluginStatus.ERRORED

        except Exception:
            self.logger.exception("Error while processing %r (%s)", file_, id_)
            return PluginStatus.FATAL
