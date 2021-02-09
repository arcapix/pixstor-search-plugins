# PixStor Search Plugin

**Name:** audio_thumbnail.py

**Author(s):** Chris Oates

**Version:** 3.0

**Last Updated:** 2019/05/21


## About This Plugin

This plugin generates thumbnail and preview images for audio file formats.

The plugin takes a 5 second sample from the audio file and generates a spectrogram image from that sample.

![Example Spectrogram](example_spectrogram.png "Example Spectrogram")


## Installing This Plugin

1. Install dependencies

**IMPORTANT** - python packages must be installed in the PixStor Search virtual environment.
To enter the virtual environment

```shell
source /usr/share/arcapix/apsearch/bin/activate
```

This plugin requires `ffmpeg`, which should have already been installed along with PixStor Search.

You will also need [numpy](http://www.numpy.org/), [scipy](https://www.scipy.org/), and [matplotlib](https://matplotlib.org/index.html).

If you're using a RedHat-based operating system, these can be installed using `yum`

``` shell
yum install numpy scipy python-matplotlib
```

Note - these are likely to be out of date. You can get the latest versions from `pip`

``` shell
pip install numpy --upgrade
pip install scipy --upgrade
pip install matplotlib --upgrade
```

**IMPORTANT** - you **must** install the yum packages **before** trying to install the pip packages.
The yum packages will install dependencies, without which you are likely to see compilation errors from pip.

Once the dependencies are installed, you can leave the virtual environment

```shell
deactivate
```

2. Download the plugin to your 'available plugins' directory

``` shell
wget -P /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras \
    https://raw.githubusercontent.com/arcapix/pixstor-search-plugins/master/community/AudioThumbnail/audio_thumbnail.py
```

3. Symlink the plugin to the 'enabled plugins' directory

``` shell
ln -s /opt/arcapix/usr/share/apsearch/plugins/available/arcapix-community-extras/audio_thumbnail.py \
    /opt/arcapix/usr/share/apsearch/plugins/enabled
```

4. Restart the `apsearch-middleware` service:

``` shell
systemctl restart apsearch-middleware
```

5. (Re)ingest content as required - existing data will not be automatically rescanned


## Using This Plugin

You can change the colour scheme of the generated image by changing the `cmap` parameter in this line

```
plt.pcolormesh(times, freqs, 10 * np.log10(Sx), cmap='viridis')
```

You can see a listing of available colour maps [here](https://matplotlib.org/examples/color/colormaps_reference.html)


## License

This plugin is licensed under the MIT License

Copyright 2019 Pixit Media Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
