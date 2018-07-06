# PixStor Search Plugin

**Name:** text.py

**Author(s):** Chris Oates

**Version:** 1.0

**Last Updated:** 2017/09/15

## About This Plugin

The `TextPlugin` extracts various attributes of a text - word count, a list of 20 commonly used words, and the language of the text.

Note - this plugin is very inefficient. It attempts to read a whole text into memory to perform its processing.
For large files, it is likely to be very slow and memory inefficient.


## Installing This Plugin

1. Install dependencies

At a minimum, you will need to install [langid](https://github.com/saffsd/langid.py)

```
pip install langid
```

Additionally, to use the `HTMLTextPlugin`, you will need [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup)

```
pip install bs4
```

for `PDFTextPlugin`, you will need textract

```
pip install textract
```

for `MSDocTextPlugin`, you will need [antiword](http://www.winfield.demon.nl/).
Instructions for installing `antiword` on Cento 7 (used by PixStor 4) can be found [here](https://centos.pkgs.org/7/forensics-x86_64/antiword-0.37-9.el7.x86_64.rpm.html)


2. Copy the plugin to your designated plugins/ directory. On a PixStor4 system, this defaults to `/opt/arcapix/usr/share/apsearch/plugins`

3. Restart the `apsearch-middleware` service:

```
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned

## Using This Plugin

The TextPlugin handles only plaintext. But it can be subclassed to handle other text-based formats.
The file includes three example subclasses - one which extracts text from MS Office Word documents,
 one which extracts text from html documents, and one which extracts text from PDF documents.

To create your own subclass, you need only provide the `_get_text` method, which extracts text from a file and returns it as a string.
Text extraction for various file formats can be found in the python [textract](http://textract.readthedocs.io/en/latest/) package.

## License

This plugin is licensed under the MIT License

Copyright 2018 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
