# PixStor Search Plugin

**Name:** phash.py

**Author(s):** Chris Oates

**Version:** 1.0

**Last Updated:** 2017/09/15

## About This Plugin

This plugin calculates the 'perceptual hash' of image files.

Unlike md5 hash, perceptual hash is based on the visual content of the image.

Images with the same hash will include exact duplicates as well as resized versions of an image.
It also has a certain tolerance for things like gamma levels, artefacts and noise.

## Installing This Plugin

1. Install dependencies

``` shell
pip install ImageHash
```

**Note**: You may also need to update scipy. The older, rpm version is incompatible with ImageHash

``` shell
pip install --upgrade scipy
```

2. Download the plugin to your 'available plugins' directory

``` shell
wget -P /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras \
    https://raw.githubusercontent.com/arcapix/pixstor-search-plugins/master/community/phash/phash.py
```

3. Symlink the plugin to the 'enabled plugins' directory

``` shell
ln -s /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras/phash.py \
    /opt/arcapix/usr/share/apsearch/plugins/enabled
```

4. Restart the `apsearch-middleware` service:

``` shell
systemctl restart apsearch-middleware
```

5. (Re)ingest content as required - existing data will not be automatically rescanned

## Using This Plugin

Similar to an md5 hash, perceptual hash can be used to search for duplicate images,
with the additional benefit that it can identify resized versions of an image.

## License

This plugin is licensed under the MIT License

Copyright 2019 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
