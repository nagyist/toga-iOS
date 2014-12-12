from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)
from toga import constants


NSLeftTextAlignment = 0
NSRightTextAlignment = 1
NSCenterTextAlignment = 2
NSJustifiedTextAlignment = 3
NSNaturalTextAlignment = 4


def NSTextAlignment(alignment):
    return {
        constants.LEFT_ALIGNED: NSLeftTextAlignment,
        constants.RIGHT_ALIGNED: NSRightTextAlignment,
        constants.CENTER_ALIGNED: NSCenterTextAlignment,
        constants.JUSTIFIED_ALIGNED: NSJustifiedTextAlignment,
        constants.NATURAL_ALIGNED: NSNaturalTextAlignment,
    }[alignment]
