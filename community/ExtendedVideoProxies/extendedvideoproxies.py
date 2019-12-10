from arcapix.search.metadata.plugins.arcapix_core.videopreview import VideoThumbnail, VideoPreview


"""
Add any additional video formats to support
"""
SUPPORTED_EXT = ['.mp4']
SUPPORTED_MIME = ['video/mp4']


class ExtendedVideoThumbnail(VideoThumbnail):
    """Generate thumbnail for additional video formats.
    By default, the builtin VideoThumbnail plugin only handles MOV.
    """

    def handles(self, ext=None, mimetype=None):
        """Override the base class handler for the video format"""
        return ext in SUPPORTED_EXT or mimetype in SUPPORTED_MIME


class ExtendedVideoPreview(VideoPreview):
    """Generate preview for additional video formats.
    By default, the builtin VideoPreview plugin only handles MOV.
    """

    def handles(self, ext=None, mimetype=None):
        """Override the base class handler for the video format"""
        return ext in SUPPORTED_EXT or mimetype in SUPPORTED_MIME
