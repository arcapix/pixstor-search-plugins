import logging
import langid
import string
from bs4 import BeautifulSoup
from collections import Counter
from textract.parsers import pdf_parser

from arcapix.search.metadata.plugins.base import Plugin, PluginStatus
from arcapix.search.metadata.helpers import Metadata
from arcapix.search.metadata.utils import execute

logger = logging.getLogger(__name__)

matchme = string.ascii_letters + string.digits


class TextPlugin(Plugin):
    """Extract metadata from text type files.

    Can be sub-classed for other text-based formats
    by overriding the ``_get_text`` method.
    """

    def namespace(self):
        return 'text'

    def handles(self, ext=None, mimetype=None):
        return (mimetype and mimetype.startswith('text/')
                and mimetype != 'text/html')

    def schema(self):
        return [
            {
            "name": "wordcount",
            "prompt": "number of words in the document",
            "value": {
                "datatype": "Long"
                }
            },
            {
            "name": "language",
            "prompt": "Primary language the text is written in",
            "value": {
                "datatype": "String"
                }
            },
            {
            "name": "common_words",
            "prompt": "Top 20 most commonly used words",
            "value": {
                "datatype": "[String]"
                }
            }
        ]

    def _get_text(self, filename):
        with open(filename, 'r') as f:
            return f.read()

    def _extract(self, filename):
        text = self._get_text(filename)

        words = get_common_strings(text)

        data = {'wordcount': sum(words.values()),
                'common_words': [k for k, _ in words.most_common(20)]}

        lang, _ = langid.classify(" ".join(k for k, _ in words.most_common(200)))

        data['language'] = lang

        return data

    def process(self, id_, file_, fileinfo=None):
        try:
            data = self._extract(file_)

            if Metadata(id_, self).update(data):
                return PluginStatus.SUCCESS

            return PluginStatus.ERRORED

        except:
            logger.exception("Error while processing %r (%s)", file_, id_)
            return PluginStatus.FATAL


class MSDocTextPlugin(TextPlugin):

    def handles(self, ext=None, mimetype=None):
        return ext == '.doc' or mimetype == 'application/msdoc'

    def _get_text(self, filename):
        return execute(["/usr/bin/antiword", filename])


class HTMLTextPlugin(TextPlugin):

    def handles(self, ext=None, mimetype=None):
        return ext in ('.htm', '.html') or mimetype == 'text/html'

    def _get_text(self, filename):
        with open(filename, 'r') as f:
            soup = BeautifulSoup(f.read(), 'html5lib')
        return " ".join(y for x in soup.find_all('p') for y in x.stripped_strings)


class PDFTextPlugin(TextPlugin):

    def handles(self, ext=None, mimetype=None):
        return ext == '.pdf' or mimetype == 'application/pdf'

    def _get_text(self, filename):
        return pdf_parser.Parser().extract(filename).decode('utf-8', 'replace')


def get_common_strings(text):
    """Find the most commonly used words in a file.
    Words are defined as alphanumeric strings
    longer than 3 characters and broken on
    whitespace and punctuation.
    """
    strings = Counter()

    words = unicode()
    for c in text.lower():
        if c in matchme:
            words += c
            continue
        if len(words) >= 4:
            strings.update([words.strip()])
        words = ""
    if len(words) >= 4:  # catch result at EOF
        strings.update([words])

    return strings
