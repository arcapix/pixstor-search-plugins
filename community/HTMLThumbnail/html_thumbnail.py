import logging
import imgkit

from arcapix.search.metadata.plugins.thumbnails import _Thumbnail

logger = logging.getLogger(__name__)


class HtmlThumbnail(_Thumbnail):
    """Create a proxy of a specified HTML file."""

    def handles(self, ext=None, mimetype=None):
        return (mimetype == 'text/html' or
                ext in ('.htm', '.html'))

    def _make_proxy(self, source_path, thumbnail_size):
        """Make a proxy image of the rendered file."""
        proxy_filename = self.generate_temp_filename(suffix='.png')

        imgkit.from_file(
            source_path,
            proxy_filename,
            options={'height': thumbnail_size[1],
                     'width': thumbnail_size[0],
                     'zoom': '0.5'}
        )

        return proxy_filename
