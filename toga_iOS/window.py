from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from .libs import UIScreen, UIWindow


class Window(object):
    def __init__(self, position=(100, 100), size=(640, 480)):
        self._app = None
        self._content = None

        self.startup()

    def startup(self):
        frame = UIScreen.mainScreen().bounds
        self._size = (frame.size.width, frame.size.height,)
        self._impl = UIWindow.alloc().initWithFrame_(frame)

    @property
    def app(self):
        return self._app

    @app.setter
    def app(self, app):
        if self._app:
            raise Exception("Window is already associated with an App")
        self._app = app

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, widget):
        self._content = widget
        self._content.window = self
        self._content.app = self.app

        # We now know the widget impl exists; add it. Top-level widgets are
        # always handled by a UIViewController, so we just use that.
        self._impl.rootViewController = self._content._controller

    def show(self):
        self._impl.makeKeyAndVisible()

    @property
    def size(self):
        return self._size
