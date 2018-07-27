from arcapix.search.metadata.plugins.thumbnails import VideoThumbnail
from arcapix.search.metadata.plugins.videopreview import VideoPreview


class ExtendedVideoThumbnail(VideoThumbnail):
    """Generate thumbnail for additional video formats.
    By default, the builtin VideoThumbnail plugin only handles MOV.
    """

    def handles(self, ext=None, mimetype=None):
        """Override the base class handler for the video format"""

        if super(ExtendedVideoThumbnail, self).handles(ext, mimetype):
            # don't handle formats already handled by builtin plugin
            return False

        """Add any additional video formats to support"""
        SUPPORTED_EXT = ('.mp4',)
        SUPPORTED_MIME = ('video/mp4',)

        return ext in SUPPORTED_EXT or mimetype in SUPPORTED_MIME


class ExtendedVideoPreview(VideoPreview):
    """Generate preview for additional video formats.
    By default, the builtin VideoPreview plugin only handles MOV.
    """

    def handles(self, ext=None, mimetype=None):
        """Override the base class handler for the video format"""

        if super(ExtendedVideoPreview, self).handles(ext, mimetype):
            # don't handle formats already handled by builtin plugin
            return False

        """Add any additional video formats to support"""
        SUPPORTED_EXT = ('.mp4',)
        SUPPORTED_MIME = ('video/mp4',)

        return ext in SUPPORTED_EXT or mimetype in SUPPORTED_MIME
