# PixStor Search Plugin

**Name:** avcodec.py

**Author(s):** Chris Oates

**Version:** 1.0

**Last Updated:** 2017/09/15

## About This Plugin

This plugin extracts information about the audio and video codecs used in video files.

## Installing This Plugin

1. Download the plugin to your 'available plugins' directory

``` shell
wget -P /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras \
    https://raw.githubusercontent.com/arcapix/pixstor-search-plugins/master/community/avcodec/avcodec.py
```

2. Symlink the plugin to the 'enabled plugins' directory

``` shell
ln -s /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras/avcodec.py \
    /opt/arcapix/usr/share/apsearch/plugins/enabled
```

3. Restart the `apsearch-middleware` service:

``` shell
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned


## Using This Plugin

This plugin allows you to search for, e.g. 'h264' or 'aac'

The plugin will attempt to handle all video formats. It could be easily adapted to work on audio files as well.


## License

This plugin is licensed under the MIT License

Copyright 2019 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
