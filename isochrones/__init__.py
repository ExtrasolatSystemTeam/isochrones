__version__ = '1.0-alpha'

try:
    __ISOCHRONES_SETUP__
except NameError:
    __ISOCHRONES_SETUP__ = False

if not __ISOCHRONES_SETUP__:
    __all__ = ['dartmouth','basti','padova',
               'Isochrone', 'StarModel']
    from .isochrone import Isochrone, get_ichrone
    from .starmodel import StarModel #, BinaryStarModel, TripleStarModel
     
