from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

import os

import toga

from ..libs import UIImage


class Icon(object):

    app_icon = None

    def __init__(self, path, system=False):
        self.path = path
        self.system = system
        if self.system:
            filename = os.path.join(
                os.path.dirname(toga.__file__), 'resources', self.path,
            )
        else:
            filename = self.path
        self._impl = UIImage.alloc().initWithContentsOfFile_(filename)

    @staticmethod
    def load(path_or_icon, default=None):
        if path_or_icon:
            if isinstance(path_or_icon, Icon):
                obj = path_or_icon
            else:
                obj = Icon(path_or_icon)
        elif default:
            obj = default
        return obj


TIBERIUS_ICON = Icon('tiberius-32.png', system=True)
