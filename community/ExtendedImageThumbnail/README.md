# PixStor Search Plugin

**Name:** extendedimagethumbnail.py

**Author(s):** Chris Oates

**Version:** 4.0

**Last Updated:** 2019/10/18


## About This Plugin

This plugin generates thumbnail and preview images for additional image formats.

The builtin `PillowThumbnail` plugin handles JPEG and DPX images.

This plugin extends the base `AbstractImageThumbnailPlugin` class to add support for additional formats.

Optional supported formats are those provided by the `ImageMagick` Libraries.
[ImageMagick supports](https://www.imagemagick.org/script/formats.php#supported)

Future iterations of the builtin `PillowThumbnail` plugin will support increased formats and as such you should ensure that any extension of an additional format does not conflict in future releases.


## Installing This Plugin

1. Download the plugin to your 'available plugins' directory

``` shell
wget -P /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras \
    https://raw.githubusercontent.com/arcapix/pixstor-search-plugins/master/community/ExtendedImageThumbnail/extendedimagethumbnail.py
```

2. Symlink the plugin to the 'enabled plugins' directory

``` shell
ln -s /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras/extendedimagethumbnail.py \
    /opt/arcapix/usr/share/apsearch/plugins/enabled
```

3. Restart the `apsearch-middleware` service:

``` shell
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned

As this plugin extended a builtin plugin it has no additional requirements.


## Using This Plugin

This plugin extends a builtin plugin to support additional image formats.

Add any image formats you want to support to the `handles` method - the `handles` method receives each file's extension and mimetype
and returns `True` or `False` depending on whether the plugin should generate a thumbnail and preview for the file.

Consideration should be given to the type image format handled.  Images with multiple layers or mip-mapped formats (E.G. PSD, EXR, Pixar TEX) are likely to cause a large memory overhead or unexpected results.  The onus is on the plugin writer to handle such formats efficiently.  It is advised to ensure successful conversion and understanding of the resource requirements of such formats outside of PixStor Search prior to implmentation.

Note: the plugin *should not* handle JPEG, DPX, PSD, PSB, or EXR images, as these are already handled by core plugins.
Handling any of these file types will cause thumbnails and previews to be generated twice, causing unwanted resource utilisation.
Database entries of prior processing results will be over-written with the data of the most recent processing event.

The call to `PillowThumbnail.handles` will prevent the plugin from handling JPEG and DPX,
plus any other formats the builtin plugin might support in the future.

The converter used to generate thumbnails is controlled by the apconfig setting `arcapix.search.proxies.image_converters`

No other changes should be necessary.


## License

This plugin is licensed under the MIT License

Copyright 2019 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
