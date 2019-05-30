from arcapix.search.metadata.plugins.arcapix_core.imagepreview import PillowThumbnail


class ExtendedImageThumbnail(PillowThumbnail):
    """Generate thumbnail and preview for additional image formats.

    By default, the builtin PillowThumbnail plugin only handles JPEG and DPX

    Note - there is also a specialised plugin for PSD, PSB, and ERX files in arcapix-core,
    so those don't need to be added to this plugin either.
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
