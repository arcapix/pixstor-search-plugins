# PixStor Search Plugin

**Name:** audio_thumbnail.py

**Author(s):** Chris Oates

**Version:** 1.0

**Last Updated:** 2018/07/06


## About This Plugin

This plugin generates thumbnail and preview images for audio file formats.

The plugin takes a 5 second sample from the audio file and generates a spectrogram image from that sample.

![Example Spectrogram](example_spectrogram.png "Example Spectrogram")


## Installing This Plugin

1. Install dependencies

This plugin requires `ffmpeg`, which should have already been installed along with PixStor Search.

You will also need [numpy](http://www.numpy.org/), [scipy](https://www.scipy.org/), and [matplotlib](https://matplotlib.org/index.html).

If you're using a RedHat-based operating system, these can be installed using `yum`

```
yum install numpy scipy python-matplotlib
```

Note - these are likely to be out of date. You can get the latest versions from `pip`

```
pip install numpy --upgrade
pip install scipy --upgrade
pip install matplotlib --upgrade
```

**IMPORTANT** - you **must** install the yum packages **before** trying to install the pip packages.
The yum packages will install dependencies, without which you are likely to see compilation errors from pip.

2. Copy the plugin to your designated plugins/ directory. On a PixStor4 system, this defaults to `/opt/arcapix/usr/share/apsearch/plugins`

3. Restart the `apsearch-middleware` service:

```
systemctl restart apsearch-middleware
```

4. (Re)ingest content as required - existing data will not be automatically rescanned


## Using This Plugin

You can change the colour scheme of the generated image by changing the `cmap` parameter in this line

```
plt.pcolormesh(times, freqs, 10 * np.log10(Sx), cmap='viridis')
```

You can see a listing of available colour maps [here](https://matplotlib.org/examples/color/colormaps_reference.html)


## License

This plugin is licensed under the MIT License

Copyright 2018 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
