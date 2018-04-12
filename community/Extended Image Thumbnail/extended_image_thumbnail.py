from arcapix.search.metadata.plugins.thumbnails import ImageThumbnail


class ExtendedImageThumbnail(ImageThumbnail):
    """Generate thumbnail and preview for additional image formats.

    By default, the builtin ImageThumbnail plugin only handles jpeg and dpx.
    """

    def handles(self, ext=None, mimetype=None):
        """Add any formats you want to support below."""
        if super(ExtendedImageThumbnail, self).handles(ext, mimetype):
            # don't handle formats already handled by builtin plugin
            return False

        # e.g. add support for png
        return ext == '.png' or mimetype == "image/png"
