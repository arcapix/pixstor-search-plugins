#PixStor Search Plugin

**Name:** allblack.py
**Author(s):** Chris Oates
**Version:** 1.0
**Last Updated:** 2017/09/15

##About This Plugin
This plugin loads each image being ingested into memory and validates whether all pixels are black (RGGB value = 0).

Care should be taken to not process extremely large images as the plugin loads the entire image into memory to perform the validation.

Users could extend this example plugin to remove the limitation of memory encapsulation via memory-mapped I/O provided by numpy or other such libraries.

##Installing This Plugin
1. Copy the plugin to your designated plugins/ directory.
2. 

##Using This Plugin
Note that this plugin will only return image which are mathmatically comprised of entirely black pixels whereby the RGB value=0. Images which are perceptually black, but which contain one or more pixels which have an RGB value != 0 will not be returned.

##License
This plugin is licensed under the MIT License

Copyright 2018 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.