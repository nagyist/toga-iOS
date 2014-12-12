from __future__ import print_function, absolute_import, division

from ..libs import UINavigationController
from .base import Widget


class NavigationContainer(Widget):

    def __init__(self, root_label, root_container):
        super(NavigationContainer, self).__init__()
        self._content = [(root_label, root_container,)]
        self.startup()

    def startup(self):
        label, container = self._content[0]
        self._prepare_for_push(label, container)
        self._controller = (
            UINavigationController.alloc().initWithRootViewController_(
                container._controller
            )
        )
        self._impl = self._controller.view

    def push(self, label, container):
        self._prepare_for_push(label, container)
        self._controller.pushViewController_animated_(
            container._controller, True,
        )
        self._content.append((label, container,))

    def pop(self):
        popped = self._controller.popViewControllerAnimated_(True)
        if popped:
            label, container = self._content.pop()
            self._react_to_pop(container)
            return container
        return None

    def pop_to_root(self):
        self._controller.popToRootViewControllerAnimated(True)
        for label, container in self._content[1:]:
            self._react_to_pop(container)
        self._content = self._content[:1]
        return [c[1] for c in self.content[1:]]

    def _prepare_for_push(self, label, container):
        container._impl.setTranslatesAutoresizingMaskIntoConstraints_(True)
        container._controller.title = label
        container.window = self.window
        container.app = self.app

    def _react_to_pop(self, container):
        container._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)
        container.window = None
        container.app = None

    def _set_app(self, app):
        for label, container in self._content:
            container.app = app

    def _set_window(self, window):
        for label, container in self._content:
            container.window = window
