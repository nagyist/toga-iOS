from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from rubicon.objc import get_selector, objc_method

from ..libs import uikit
from .base import Widget


class ButtonImpl(uikit.UIButton):
    @objc_method('v@')
    def onPress_(self, obj):
        print('in on_press handler')
        interface = self.__dict__['interface']
        if interface.on_press:
            interface.on_press(interface)


class Button(Widget):
    def __init__(self, label, on_press=None):
        super(Button, self).__init__()

        self.on_press = on_press
        self.label = label

        self.startup()

    def startup(self):
        self._impl = ButtonImpl.alloc().init()
        self._impl.__dict__['interface'] = self

        self._impl.setTitle_forState_(self.label, uikit.UIControlStateNormal)
        self._impl.setTitleColor_forState_(
            uikit.UIColor.blackColor(), uikit.UIControlStateNormal,
        )
        self._impl.addTarget_action_forControlEvents_(
            self._impl, get_selector('onPress:'),
            uikit.UIControlEventTouchDown,
        )

        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)
