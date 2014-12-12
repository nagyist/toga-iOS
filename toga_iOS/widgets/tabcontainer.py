from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from rubicon.objc import objc_method

from ..libs import uikit, NSArray, NSObject
from .base import Widget


def _hug(superview, subview):
    for i in (uikit.NSLayoutAttributeBottom, uikit.NSLayoutAttributeLeft,
              uikit.NSLayoutAttributeRight, uikit.NSLayoutAttributeTop):
        constraint = uikit.NSLayoutConstraint.constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
            superview, i, uikit.NSLayoutRelationEqual,
            subview, i, 1, 0,
        )
        superview.addConstraint_(constraint)


class TabContainerImplHelper(NSObject):

    # UITabVarControllerDelegate
    @objc_method('v@@')
    def tabBarController_didSelectViewController_(self, tbc, vc):
        """Perform subsequent layout for tabs not initially shown.
        """
        _hug(tbc.view, vc.view)


class TabContainerImpl(uikit.UITabBarController):

    @objc_method('v')
    def viewDidLayoutSubviews(self):
        """Performs initial layout for the first tab shown.
        """
        _hug(self.view, self.selectedViewController.view)


class TabContainer(Widget):

    def __init__(self):
        super(TabContainer, self).__init__()
        self._content = []
        self.startup()

    def startup(self):
        self._controller = TabContainerImpl.alloc().init()
        self._controller.setDelegate_(TabContainerImplHelper.alloc().init())
        self._impl = self._controller.view
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    def add(self, label, icon, container):
        self._content.append((label, icon, container,))
        container.window = self.window
        container.app = self.app
        container._controller.tabBarItem.title = label
        container._controller.tabBarItem.image = icon._impl if icon else None

        controllers = self._controller.viewControllers
        if controllers is None:
            controllers = NSArray.arrayWithObject_(container._controller)
        else:
            controllers = controllers.mutableCopy()
            controllers.addObject_(container._controller)
        self._controller.setViewControllers_animated_(controllers, True)

    def _set_window(self, window):
        for label, icon, child in self._content:
            child.window = window

    def _set_app(self, app):
        for label, icon, child in self._content:
            child.app = app
