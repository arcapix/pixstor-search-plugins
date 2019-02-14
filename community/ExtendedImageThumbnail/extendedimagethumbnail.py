from arcapix.search.metadata.plugins.arcapix_core.thumbnails import ImageThumbnail


class ExtendedImageThumbnail(ImageThumbnail):
    """Generate thumbnail and preview for additional image formats.

    By default, the builtin ImageThumbnail plugin only handles JPEG and DPX.
    """

    def handles(self, ext=None, mimetype=None):
        """Override the base class handler for the image format"""

        if super(ExtendedImageThumbnail, self).handles(ext, mimetype):
            # don't handle formats already handled by builtin plugin
            return False

        """Add any additional image formats to support"""
        SUPPORTED_EXT = ('.png', '.rgb')
        SUPPORTED_MIME = ('image/png', 'image/rgb', 'image/x-rgb')

        return ext in SUPPORTED_EXT or mimetype in SUPPORTED_MIME
