from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from ..libs import UIScreen, UIScrollView, UIViewController
from .base import Widget


class ScrollContainer(Widget):
    def __init__(self, horizontal=True, vertical=True):
        super(ScrollContainer, self).__init__()
        self.horizontal = horizontal
        self.vertical = vertical
        self._content = None
        self.startup()

    def startup(self):
        frame = UIScreen.mainScreen().applicationFrame
        self._controller = UIViewController.alloc().init()
        self._impl = UIScrollView.alloc().initWithFrame_(frame)
        self._controller.view = self._impl

        self._impl.showsVerticalScrollIndicator = self.vertical
        self._impl.showsHorizontalScrollIndicator = self.horizontal
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, widget):
        self._content = widget
        self._content.window = self.window
        self._content.app = self.app
        self._impl.addSubview_(widget._impl)
        self._impl.contentSize = widget._impl.frame().size

    def _set_window(self, window):
        self._content.window = window

    def _set_app(self, app):
        self._content.app = app
