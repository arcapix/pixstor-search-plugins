# PixStor Search Plugin

**Name:** colours.py

**Author(s):** Chris Oates

**Version:** 2.0

**Last Updated:** 2019/10/18

## About This Plugin

This plugin identifies the 10 most commonly appearing colours in an image.

This is done using [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) to pick out the 10 most common colours in RGB.
The RGB values are then translated in to the nearest colour name from the [web colours](https://en.wikipedia.org/wiki/Web_colors) set.

Note - the plugin may return fewer than 10 colours if 10 unique colours can't be identified in the image

## Installing This Plugin

1. Install dependencies

**IMPORTANT** - python packages must be installed in the PixStor Search virtual environment.
To enter the virtual environment

```shell
source /usr/share/arcapix/apsearch/bin/activate
```

To use this plugin will need [numpy](http://www.numpy.org/) and [scipy](https://www.scipy.org/).

If you're using a RedHat-based operating system, these can be installed using `yum`

``` shell
yum install numpy scipy
```

Note - these are likely to be out of date. You can get the latest versions from `pip`

``` shell
pip install numpy --upgrade
pip install scipy --upgrade
```

**IMPORTANT** - you **must** install the yum packages **before** trying to install the pip packages.
The yum packages will install dependencies, without which you are likely to see compilation errors from pip.

You will also need the python webcolors package

``` shell
pip install webcolors
```

Once the dependencies are installed, you can leave the virtual environment

```shell
deactivate
```

2. Download the plugin to your 'available plugins' directory

``` shell
wget -P /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-supported-extras \
    https://raw.githubusercontent.com/arcapix/pixstor-search-plugins/master/supported/colours/colours.py
```

3. Symlink the plugin to the 'enabled plugins' directory

``` shell
ln -s /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-supported-extras/colours.py \
    /opt/arcapix/usr/share/apsearch/plugins/enabled
```

4. Restart the `apsearch-middleware` service:

``` shell
systemctl restart apsearch-middleware
```

5. (Re)ingest content as required - existing data will not be automatically rescanned

## Using This Plugin

This plugin makes it possible to search for images by colour - for example, find images which are predominately red.

Note - this plugin may be slow, especially for larger images. To make things a little faster, images are scaled-down prior to clustering. Some colours may be lost as a side-effect of this scaling-down.

This plugin will attempt to handle all image file formats. In practice, it should be able to handle an image format that ImageMagick can handle.

## License

This plugin is licensed under the MIT License

Copyright 2019 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
