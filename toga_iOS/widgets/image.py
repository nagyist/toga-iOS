from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

import os
from ctypes import c_char_p

import toga

from ..libs import (
    NSData, UIImage, UIImageView, UIViewContentModeScaleAspectFit,
)
from .base import Widget


class Image(object):

    def __init__(self, data):
        if data:
            objc_data = NSData.alloc().initWithBytes_length_(
                c_char_p(data), len(data),
            )
        else:
            objc_data = None
        self._impl = UIImage.alloc().initWithData_(objc_data)

    @classmethod
    def load(cls, path, system=False):
        if system:
            path = os.path.join(
                os.path.dirname(toga.__file__), 'resources', path,
            )
        with open(path) as f:
            image = cls(f.read())
        return image


class ImageView(Widget):

    def __init__(self, image):
        super(ImageView, self).__init__()
        self._image = image

        self.startup()

    def startup(self):
        self._impl = UIImageView.alloc().initWithImage_(self.image._impl)
        # TODO: Add constants in Toga for customisation.
        self._impl.setContentMode_(UIViewContentModeScaleAspectFit)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        if not isinstance(value, Image):
            value = Image.load(value)
        self._image = value
        self._impl.image = value._impl
