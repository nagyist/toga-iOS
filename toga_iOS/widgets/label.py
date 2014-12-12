from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from toga.constants import LEFT_ALIGNED

from ..libs import UILabel, NSTextAlignment, NSLineBreakByWordWrapping
from .base import Widget


class Label(Widget):
    def __init__(self, text=None, alignment=LEFT_ALIGNED):
        super(Label, self).__init__()

        self.startup()

        self.alignment = alignment
        self.text = text

    def startup(self):
        self._impl = UILabel.new()
        self._impl.lineBreakMode = NSLineBreakByWordWrapping
        self._impl.numberOfLines = 99999    # Always allow multi-lin labels.
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    @property
    def alignment(self):
        return self._alignment

    @alignment.setter
    def alignment(self, value):
        self._alignment = value
        self._impl.setTextAlignment_(NSTextAlignment(self._alignment))

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._impl.setText_(self._text)
