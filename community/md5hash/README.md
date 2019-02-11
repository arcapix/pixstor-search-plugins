# PixStor Search Plugin

**Name:** md5hash.py

**Author(s):** Chris Oates

**Version:** 2.0

**Last Updated:** 2019/02/11

## About This Plugin

This plugin calculates the md5 hash sum of every file on the filesystem.

This offers an alternative the the sha512-based hash plugin distributed with PixStor Search.

Note - this is likely to be very slow, especially for large files.

## Installing This Plugin

1. Copy the plugin to your designated plugins directory. On a PixStor4 system, this defaults to `/opt/arcapix/usr/share/apsearch/plugins/available/user`

2. Create a symlink into the enabled plugins directory `/opt/arcapix/usr/share/apsearch/plugins/enabled`

3. Restart the `apsearch-middleware` service:

```
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned

## Using This Plugin

This plugin could be used as the basis for finding duplicate files. Once you know the hash of a particular file, you can search for any other files which has the same hash. The search results must have the exact same contents.

A duplicate finding tool is distributed with PixStor Search. To use it with this plugin, all you need to do is specify the plugin's hash field name

```
find_duplicates --hash-field core.hash.md5
```


## License

This plugin is licensed under the MIT License

Copyright 2019 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
