import webcolors
import scipy as sp
import scipy.cluster as cluster

from arcapix.search.metadata.plugins.base import Plugin, PluginStatus
from arcapix.search.metadata.helpers import Metadata
from arcapix.search.metadata.utils import load_image


class ColoursPlugin(Plugin):
    """Example plugin to extract a list of common colours from an image."""

    def namespace(self):
        return 'image'

    def handles(self, ext=None, mimetype=None):
        return mimetype and mimetype.startswith('image/')

    def schema(self):
        return [{
            "name": "colours",
            "prompt": "Names of common colours extracted from the image",
            "value": {
                "datatype": "[String]"  # list of strings
            }
        }]

    def _extract(self, filename):
        rgb = get_most_common_colours(filename)
        names = set(get_colour_name(colour, 'css21') for colour in rgb)
        names.update(set(get_colour_name(colour, 'css3') for colour in rgb))

        return {'colours': list(names)}

    def process(self, id_, file_, fileinfo=None):
        try:
            data = self._extract(file_)

            if Metadata(id_, self).update(data):
                return PluginStatus.SUCCESS

            return PluginStatus.ERRORED

        except Exception as e:
            self.logger.error(
                "An exception was raised while processing '%s' (%s) with %s - %s: %s",
                file_, id_, self.__class__.__name__, e.__class__.__name__, e)
            self.logger.debug("Traceback while processing %r (%s)", file_, id_, exc_info=True)
            return PluginStatus.FATAL


# http://stackoverflow.com/a/9694246
def get_colour_name(requested_colour, spec='css3'):
    """Get colour name for an RGB tuple.
    Colour names can be those from css2 (simpler)
    or css3 (more flowery)
    """
    try:
        return webcolors.rgb_to_name(requested_colour, spec)
    except ValueError:
        pass

    colours = getattr(webcolors, '%s_hex_to_names' % spec).items()
    min_colours = {}

    for key, name in colours:
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name

    return min_colours[min(min_colours.keys())]


# http://stackoverflow.com/a/3244061
def get_most_common_colours(filename):
    """Returns a list of RGB tuples.
    Returns up to 10 most common colours for
    an image based on k-mean clustering
    (in no particular order).
    """
    NUM_CLUSTERS = 10

    im = load_image(filename)
    im.shrink((150, 150))
    ar = im.to_numpy()

    shape = ar.shape
    ar = ar.reshape(sp.product(shape[:2]), shape[2])

    codes, _ = cluster.vq.kmeans(ar, NUM_CLUSTERS)

    return codes.astype(int)
