# PixStor Search Plugin

**Name:** colourfulness.py

**Author(s):** Chris Oates

**Version:** 3.0

**Last Updated:** 2019/10/18

## About This Plugin

This plugin calculates a metric of _colourfulness_ of an image.

Colourfulness is measured on a scale of 0-6, where 0 is black-and-white, and 6 is most colourful.

The calculation is based on an article from [pyimagesearch](http://www.pyimagesearch.com/2017/06/05/computing-image-colorfulness-with-opencv-and-python/)

## Installing This Plugin

1. Download the plugin to your 'available plugins' directory

``` shell
wget -P /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras \
    https://raw.githubusercontent.com/arcapix/pixstor-search-plugins/master/community/colourfulness/colourfulness.py
```

2. Symlink the plugin to the 'enabled plugins' directory

``` shell
ln -s /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras/colourfulness.py \
    /opt/arcapix/usr/share/apsearch/plugins/enabled
```

3. Restart the `apsearch-middleware` service:

``` shell
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned


## Using This Plugin

The colourfulness metric works well as a filter field - for example, search for images cityscapes, filter by colourfulness=0 (black and white)

Alternatively, the plugin could be adapted to apply specific labels to images based on colourfulness, such as 'black and white', 'vibrant', etc.


## License

This plugin is licensed under the MIT License

Copyright 2019 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
