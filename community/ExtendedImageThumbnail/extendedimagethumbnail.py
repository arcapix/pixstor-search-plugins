from arcapix.search.metadata.plugins.arcapix_core.imagepreview import AbstractImageThumbnailPlugin
from arcapix.search.metadata.plugins.arcapix_core.imagepreview import PillowThumbnail as CoreImageThumbnail


"""
Add any additional image formats to support
"""
SUPPORTED_EXT = ['.png', '.rgb']
SUPPORTED_MIME = ['image/png', 'image/rgb', 'image/x-rgb']


class ExtendedImageThumbnail(AbstractImageThumbnailPlugin):
    """Generate thumbnail and preview for additional image formats.

    By default, the core Image Thumbnail plugin only handles JPEG and DPX

    Note - there is also a specialised plugin for PSD, PSB, and ERX files in arcapix-core,
    so those don't need to be added to this plugin either.
    """

    def _load_image(self, source_path):
        return AbstractImageThumbnailPlugin._load_image(self, source_path)

    def handles(self, ext=None, mimetype=None):
        """Override the base class handler for the image format"""

        if CoreImageThumbnail().handles(ext, mimetype):
            # don't handle formats already handled by builtin plugin
            return False

        return ext in SUPPORTED_EXT or mimetype in SUPPORTED_MIME
