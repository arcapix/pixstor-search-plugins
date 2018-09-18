# PixStor Search Plugin

**Name:** hash.py

**Author(s):** Chris Oates

**Version:** 1.0

**Last Updated:** 2017/09/15

## About This Plugin

This plugin calculates the md5 hash sum of every file on the filesystem.

Note - this is likely to be very slow, especially for large files.

## Installing This Plugin

1. Copy the plugin to your designated plugins/ directory. On a PixStor4 system, this defaults to `/opt/arcapix/usr/share/apsearch/plugins`

2. Restart the `apsearch-middleware` service:

```
systemctl restart apsearch-middleware
```

3. (Re)ingest content as required - existing data will not be automatically rescanned

## Using This Plugin

This plugin could be used as the basis for finding duplicate files. Once you know the hash of a particular file, you can search for any other files which has the same hash. The search rules must have the exact same contents.

This could be especially useful when used via search's REST interface - one could, for example, write a de-duping script which searches for and deletes files matching a particular hash.

## License

This plugin is licensed under the MIT License

Copyright 2018 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
