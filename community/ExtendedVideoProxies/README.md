# PixStor Search Plugin

**Name:** extendedvideoproxies.py

**Author(s):** Chris Oates

**Version:** 1.0

**Last Updated:** 2018/07/25


## About This Plugin

This plugin generates thumbnail and preview videos for additional video formats.

The builtin `VideoThumbnail` and `VideoPreview` plugins handle only MOV (quicktime) files.

This plugin overrides the builtin plugin's `handles` method to add support for additional formats.

Optional supported formats are those provided by the `ffmpeg` Libraries.
[ffmpeg supports](https://ffmpeg.org/ffmpeg-formats.html)

Future iterations of the builtin plugins may support increased formats and as such
you should ensure that any extension of an additional format does not conflict in future releases.


## Installing This Plugin

1. Copy the plugin to your designated plugins/ directory. On a PixStor4 system, this defaults to `/opt/arcapix/usr/share/apsearch/plugins`

2. Restart the `apsearch-middleware` service:

```
systemctl restart apsearch-middleware
```

3. (Re)ingest content as required - existing data will not be automatically rescanned

As this plugin extended a builtin plugin it has no additonal requirements.


## Using This Plugin

This plugin extends builtin plugins to support additional video formats.

Add any video formats you want to support to the `handles` method - the `handles` method receives each file's extension and mimetype
and returns `True` or `False` depending on whether the plugins should generate a thumbnail and preview for the file.

Note: the plugin *should not* handle MOV images as these are already handled by the builtin plugins.
Handling MOV will cause thumbnails and previews to be generated twice for those formats causing unwanted resource utilisation. 
Database entries of prior processing results will be over-written with the data of the most recent processing event.

The `super` call in the example will prevent the plugins from handling MOV,
plus any other formats the builtin plugin might support in the future.

No other changes should be necessary.


## License

This plugin is licensed under the MIT License

Copyright 2018 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
