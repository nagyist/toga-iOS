from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from rubicon.objc import objc_method
from toga.constraint import Attribute, Constraint

from ..libs import uikit
from .base import Widget


class ContainerImplHelper(uikit.UIViewController):

    @objc_method('v')
    def viewDidLayoutSubviews(self):
        # HACK: If this is the content view of a scroll view, update the
        # scroll view's content size to fit.
        superview = self.view.superview()
        if superview.__dict__['objc_class'] is uikit.UIScrollView:
            superview.contentSize = self.view.frame().size


class Container(Widget):

    _IDENTIFIER = {
        None: uikit.NSLayoutAttributeNotAnAttribute,
        Attribute.LEFT: uikit.NSLayoutAttributeLeft,
        Attribute.RIGHT: uikit.NSLayoutAttributeRight,
        Attribute.TOP: uikit.NSLayoutAttributeTop,
        Attribute.BOTTOM: uikit.NSLayoutAttributeBottom,
        Attribute.LEADING: uikit.NSLayoutAttributeLeading,
        Attribute.TRAILING: uikit.NSLayoutAttributeTrailing,
        Attribute.WIDTH: uikit.NSLayoutAttributeWidth,
        Attribute.HEIGHT: uikit.NSLayoutAttributeHeight,
        Attribute.CENTER_X: uikit.NSLayoutAttributeCenterX,
        Attribute.CENTER_Y: uikit.NSLayoutAttributeCenterY,
        # Attribute.BASELINE: uikit.NSLayoutAttributeBaseline,
    }

    _RELATION = {
        Constraint.LTE: uikit.NSLayoutRelationLessThanOrEqual,
        Constraint.EQUAL: uikit.NSLayoutRelationEqual,
        Constraint.GTE: uikit.NSLayoutRelationGreaterThanOrEqual,
    }

    def __init__(self):
        super(Container, self).__init__()
        self.children = []
        self.constraints = {}

        self.startup()

    def startup(self):
        frame = uikit.UIScreen.mainScreen().applicationFrame
        self._controller = ContainerImplHelper.alloc().init()
        self._impl = uikit.UIView.alloc().initWithFrame_(frame)

        # http://stackoverflow.com/questions/17745571
        self._controller.edgesForExtendedLayout = uikit.UIRectEdgeNone
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)
        self._controller.view = self._impl

    def add(self, widget):
        self.children.append(widget)

        # Assign the widget to the same app as the window.
        widget.app = self.app
        widget.window = self.window

        self._impl.addSubview_(widget._impl)

    def _set_app(self, app):
        for child in self.children:
            child.app = app

    def _set_window(self, window):
        for child in self.children:
            child.window = window

    def constrain(self, *constraints):
        "Add the given constraint to the widget."

        for constraint in constraints:
            if constraint in self.constraints:
                continue

            widget = constraint.attr.widget._impl
            identifier = constraint.attr.identifier

            if constraint.related_attr:
                related_widget = constraint.related_attr.widget._impl
                related_identifier = constraint.related_attr.identifier

                multiplier = (
                    constraint.related_attr.multiplier
                    / constraint.attr.multiplier
                )
                constant = (
                    (constraint.related_attr.constant - constraint.attr.constant)
                    / constraint.attr.multiplier
                )

            else:
                related_widget = None
                related_identifier = None

                multiplier = constraint.attr.multiplier
                constant = constraint.attr.constant

            constraint._impl = uikit.NSLayoutConstraint.constraintWithItem_attribute_relatedBy_toItem_attribute_multiplier_constant_(
                widget, self._IDENTIFIER[identifier],
                self._RELATION[constraint.relation],
                related_widget, self._IDENTIFIER[related_identifier],
                multiplier, constant,
            )

            self._impl.addConstraint_(constraint._impl)
            self.constraints[constraint] = constraint._impl
