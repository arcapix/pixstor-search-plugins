import logging
from PIL import Image
from anythumbnailer.thumbnail_ import thumbnailer_for, Unoconv

from arcapix.search.metadata.plugins.arcapix_core.imagepreview import AbstractThumbnailPlugin
from arcapix.search.metadata.utils import image_to_thumbnail, get_mimetype

logger = logging.getLogger('arcapix.search.metadata.plugins.ext.document_thumbnail')


class DocumentThumbnail(AbstractThumbnailPlugin):
    """Create a proxy for various document types.

    Uses anythumbnailer, which covers a lot
    of document types including pdf, and ms docs
    For unsupported file types, anythumbnailer
    will return None, rather than raise an error.

    Anythumbnailer has a 'create_thumbnail' public method
    but it relies on ``mimetype.guess_type``.
    This method is not very reliable, and since
    we already have the actual mimtype from
    metadata extraction, we can use the
    ``thumbnailer_for`` method instead.

    Note also, anythumbnailer can't identify
    openoffice formats, so we fallback on unoconv
    if ``thumbnailer_for`` fails to return anything.
    """

    def namespace(self):
        return 'document'

    def handles(self, ext=None, mimetype=None):
        return (mimetype and mimetype.startswith('application/') and
                # files which can't be identified usually return mimetype application/octet-stream
                # so we skip these, as they're likely to fail
                mimetype != 'application/octet-stream')

    def _make_proxy(self, source_path, thumbnail_size):
        mimetype = get_mimetype(source_path)
        thumbnailer = thumbnailer_for(mimetype)

        # fallback on unoconv - can handle most doc formats
        if thumbnailer is None:
            thumbnailer = Unoconv()

        logger.debug("Using thumbnailer %r for %r (mimetype=%s)",
                     thumbnailer, source_path, mimetype)

        bytes_ = thumbnailer.thumbnail(source_path)

        if bytes_ is None:
            logger.warn("Couldn't create a document thumbnail for %r", source_path)
            raise Exception("Document thumbnail couldn't be created")

        img = Image.open(bytes_)
        img = image_to_thumbnail(img, thumbnail_size)

        proxy_filename = self.generate_temp_filename(suffix='.png')

        img.save(proxy_filename, 'PNG', optimize=True)

        return proxy_filename
