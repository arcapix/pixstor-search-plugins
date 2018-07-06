# PixStor Search Plugin

**Name:** document_thumbnail.py

**Author(s):** Chris Oates

**Version:** 1.0

**Last Updated:** 2018/07/06


## About This Plugin

This plugin generates thumbnail and preview images for document file formats - including PDF and Word


## Installing This Plugin

1. Install dependencies

This plugin uses [Anythumbnailer](https://github.com/FelixSchwarz/anythumbnailer),
which should have been installed along with PixStor Search

In addition, to generate thumbnails for pdf formats you will need [poppler](https://poppler.freedesktop.org/) and [netpbm](http://netpbm.sourceforge.net/)

```
yum install poppler poppler-utils
yum install netpbm netpbm-progs
```

For 'office' formats (Microsoft Office, OpenOffice, LibreOffice), you will need [unoconv](https://github.com/dagwieers/unoconv)

```
yum install unoconv
```

2. Copy the plugin to your designated plugins/ directory. On a PixStor4 system, this defaults to `/opt/arcapix/usr/share/apsearch/plugins`

3. Restart the `apsearch-middleware` service:

```
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned


## Using This Plugin

Currently, the plugin will try to handle any file with an 'application' mimetype. This covers all document formats.
However, there are other application mimeytypes for which the plugin is likely to fail.

You may prefer to change the `handles` method to cover only a specific set of document formats.


## License

This plugin is licensed under the MIT License

Copyright 2018 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
