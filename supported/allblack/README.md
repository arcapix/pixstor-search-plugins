# PixStor Search Plugin

**Name:** allblack.py

**Author(s):** Chris Oates

**Version:** 2.0

**Last Updated:** 2019/10/18


## About This Plugin

This plugin loads each image being ingested into memory and validates whether all pixels are black (RGB value = 0).

Use case: identify redundant scanner data

In the case where a scanner fails to generate an image, it will produce a completely black images file.
This plugin will flag such files, making them easy to identify.

Outside of the Search UI, one could write a script that interfaces directly with the middleware to find and remove such files.


## Installing This Plugin

1. Download the plugin to your 'available plugins' directory

``` shell
wget -P /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-supported-extras \
    https://raw.githubusercontent.com/arcapix/pixstor-search-plugins/master/supported/allblack/allblack.py
```

2. Symlink the plugin to the 'enabled plugins' directory

``` shell
ln -s /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-supported-extras/allblack.py \
    /opt/arcapix/usr/share/apsearch/plugins/enabled
```

3. Restart the `apsearch-middleware` service:

``` shell
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned

Note: this plugin requires numpy, which should already be installed along with PixStor Search.


## Using This Plugin

This plugin will only return image which are mathematically comprised of entirely black pixels whereby the RGB value=0. Images which are perceptually black, but which contain one or more pixels which have an RGB value != 0 will not be returned.

Care should be taken to not process extremely large images as the plugin loads the entire image into memory to perform the validation.

Users could extend this example plugin to remove the limitation of memory encapsulation via memory-mapped I/O provided by numpy or other such libraries.


## License

This plugin is licensed under the MIT License

Copyright 2019 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
