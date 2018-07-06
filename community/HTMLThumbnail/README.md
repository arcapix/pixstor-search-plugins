# PixStor Search Plugin

**Name:** html_thumbnail.py

**Author(s):** Chris Oates

**Version:** 1.0

**Last Updated:** 2018/07/06


## About This Plugin

This plugin generates thumbnail and preview images for html documents.

It attempts to generate an image of the document as it would appear in a web browser.


## Installing This Plugin

1. Install dependencies

This plugin uses the python [imgkit](https://github.com/jarrekk/imgkit) package to generate the images.

In turn, `imgkit` requires [wkhtmltopdf](https://wkhtmltopdf.org/). For RedHat-based systems, there is no `yum` repo.
If you are using Centos 7 (as is the case for PixStor 4 systems), you can follow the instructions [here](https://gist.github.com/AndreasFurster/ebe3f163d6d47be43b72b35b18d8b5b6)

Once `wkhtmltopdf` is installed, you can install `imgkit` from `pip`

```
pip install imgkit
```

2. Copy the plugin to your designated plugins/ directory. On a PixStor4 system, this defaults to `/opt/arcapix/usr/share/apsearch/plugins`

3. Restart the `apsearch-middleware` service:

```
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned


## Using This Plugin

If the html document uses external files - such as scripts or stylesheets - you may find the image doesn't render correctly (or at all).


## License

This plugin is licensed under the MIT License

Copyright 2018 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
