# PixStor Search Plugin

**Name:** colours.py

**Author(s):** Chris Oates

**Version:** 1.0

**Last Updated:** 2017/09/15

## About This Plugin

This plugin identifies the 10 most commonly appearing colours in an image.

This is done using [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) to pick out the 10 most common colours in RGB.
The RGB values are then translated in to the nearest colour name from the [web colours](https://en.wikipedia.org/wiki/Web_colors) set.

Note - the plugin may return fewer than 10 colours if 10 unique colours can't be identified in the image

## Installing This Plugin

1. Install dependencies

You will also need [numpy](http://www.numpy.org/) and [scipy](https://www.scipy.org/).

If you're using a RedHat-based operating system, these can be installed using `yum`

```
yum install numpy scipy
```

Note - these are likely to be out of date. You can get the latest versions from `pip`

```
pip install numpy --upgrade
pip install scipy --upgrade
```

**IMPORTANT** - you **must** install the yum packages **before** trying to install the pip packages.
The yum packages will install dependencies, without which you are likely to see compilation errors from pip.

You will also need the python webcolors package

```
pip install webcolors
```

2. Copy the plugin to your designated plugins/ directory. On a PixStor4 system, this defaults to `/opt/arcapix/usr/share/apsearch/plugins`

3. Restart the `apsearch-middleware` service:

```
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned

## Using This Plugin

This plugin makes it possible to search for images by colour - for example, find images which are predominately red.

Note - this plugin may be slow, especially for larger images. To make things a little faster, images are scaled-down prior to clustering. Some colours may be lost as a side-effect of this scaling-down.

This plugin will attempt to handle all image file formats. In practice, it should be able to handle an image format that ImageMagick can handle.

## License

This plugin is licensed under the MIT License

Copyright 2018 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
