import logging
import os
import re
import textwrap
from bs4 import BeautifulSoup
from itertools import ifilter
from PIL import Image, ImageDraw, ImageFont

from arcapix.search.metadata.plugins.base import ThumbnailPlugin

logger = logging.getLogger('arcapix.search.metadata.plugins.ext.text_thumbnail')

# path to the font files
FONTS_PATH = os.path.abspath(__file__ + '/../fonts/')


class TextThumbnail(ThumbnailPlugin):
    """Create a proxy of a specified Text file."""

    def namespace(self):
        return 'text'

    def handles(self, ext=None, mimetype=None):
        return (mimetype and mimetype.startswith('text/') and
                not mimetype == 'text/html')  # handled by subclass below

    def _get_text(self, source_path):
        with open(source_path, 'r') as f:
            # Don't bother reading the whole thing
            # since it won't fit on the proxy anyway
            text = str(f.read(8192))

        return text

    def _get_text_lines(self, source_path, wrap_width=40):
        text = self._get_text(source_path)

        lines = textwrap.wrap(text, wrap_width)
        num_lines = len(lines)

        if num_lines > 100:
            lines = lines[50:]

        return lines

    def _make_proxy(self, source_path, thumbnail_size):

        title_font = ImageFont.truetype(os.path.join(FONTS_PATH, "MavenPro-Bold.ttf"), 20)
        main_font = ImageFont.truetype(os.path.join(FONTS_PATH, "MavenPro-Regular.ttf"), 18)

        wrap_width = int((thumbnail_size[0] - 40.) / main_font.getsize('x')[0])

        title = os.path.basename(source_path)
        lines = (str(x) for x in self._get_text_lines(source_path, wrap_width))

        image = Image.new("RGBA", thumbnail_size, (255, 255, 255))
        draw = ImageDraw.Draw(image)

        _, height = title_font.getsize(title)
        x_pos = 20
        y_pos = 20

        draw.text((x_pos, y_pos), title, (0, 0, 0), font=title_font)
        y_pos = height + 40

        for line in lines:
            _, height = main_font.getsize(line)

            draw.text((x_pos, y_pos), line, (0, 0, 0), font=main_font)
            y_pos += height
            if y_pos > (thumbnail_size[1] - 20):
                break

        proxy_filename = self.generate_temp_filename(suffix='.png')

        image.save(proxy_filename, 'PNG', optimize=True)

        return proxy_filename


class HtmlTextThumbnail(TextThumbnail):
    """Create a proxy of a specified HTML file."""

    def handles(self, ext=None, mimetype=None):
        return (mimetype == 'text/html' or
                ext in ('.htm', '.html'))

    def _get_text(self, source_path):
        """Extract just the readable text from the HTML.
        This is passed to the other functions
        in the parent class to make the image
        """
        html = super(HtmlTextThumbnail, self)._get_text(source_path)
        soup = BeautifulSoup(html)
        texts = soup.findAll(text=True)

        def visible(element):
            if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
                return False
            elif re.match('<!--.*-->', str(element)):
                return False
            elif re.match('\n', str(element)):
                return False
            return True

        visible_text = re.sub(r'[\t\n\r]', ' ', " ".join(ifilter(visible, texts)))

        return visible_text
