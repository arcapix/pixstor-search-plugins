# PixStor Search Plugin

**Name:** document_thumbnail.py

**Author(s):** Chris Oates

**Version:** 3.0

**Last Updated:** 2019/05/21


## About This Plugin

This plugin generates thumbnail and preview images for document file formats - including PDF and Word

![Example PDF Thumbnail](example_pdf_thumbnail.png "Example PDF Thumbnail")

## Installing This Plugin

1. Install dependencies

This plugin uses [Anythumbnailer](https://github.com/FelixSchwarz/anythumbnailer),
which should have been installed along with PixStor Search

In addition, to generate thumbnails for pdf formats you will need [poppler](https://poppler.freedesktop.org/) and [netpbm](http://netpbm.sourceforge.net/)

``` shell
yum install poppler poppler-utils
yum install netpbm netpbm-progs
```

For 'office' formats (Microsoft Office, OpenOffice, LibreOffice), you will need [unoconv](https://github.com/dagwieers/unoconv)

``` shell
yum install unoconv
```

2. Download the plugin to your 'available plugins' directory

``` shell
wget -P /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras \
    https://raw.githubusercontent.com/arcapix/pixstor-search-plugins/master/community/DocumentThumbnail/document_thumbnail.py
```

3. Symlink the plugin to the 'enabled plugins' directory

``` shell
ln -s /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras/document_thumbnail.py \
    /opt/arcapix/usr/share/apsearch/plugins/enabled
```

4. Restart the `apsearch-middleware` service:

``` shell
systemctl restart apsearch-middleware
```

5. (Re)ingest content as required - existing data will not be automatically rescanned


## Using This Plugin

Currently, the plugin will try to handle any file with an 'application' mimetype. This covers all document formats.
However, there are other application mimeytypes for which the plugin is likely to fail.

You may prefer to change the `handles` method to cover only a specific set of document formats.


## License

This plugin is licensed under the MIT License

Copyright 2019 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
