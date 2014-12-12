from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)
from ctypes import Structure
from rubicon.objc import CGFloat


UIRectEdgeNone = 0
UIRectEdgeTop = 1 << 0
UIRectEdgeLeft = 1 << 1
UIRectEdgeBottom = 1 << 2
UIRectEdgeRight = 1 << 3
UIRectEdgeAll = (
    UIRectEdgeTop | UIRectEdgeLeft | UIRectEdgeBottom | UIRectEdgeRight
)


class UIEdgeInsets(Structure):
    _fields_ = [
        ('top', CGFloat),
        ('left', CGFloat),
        ('bottom', CGFloat),
        ('right', CGFloat),
    ]


def UIEdgeInsetsMake(top, left, bottom, right):
    return UIEdgeInsets(top, left, bottom, right)
