from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)
from rubicon.objc import ObjCClass


NSLayoutConstraint = ObjCClass('NSLayoutConstraint')

NSLayoutRelationLessThanOrEqual = -1
NSLayoutRelationEqual = 0
NSLayoutRelationGreaterThanOrEqual = 1

NSLayoutAttributeLeft = 1
NSLayoutAttributeRight = 2
NSLayoutAttributeTop = 3
NSLayoutAttributeBottom = 4
NSLayoutAttributeLeading = 5
NSLayoutAttributeTrailing = 6
NSLayoutAttributeWidth = 7
NSLayoutAttributeHeight = 8
NSLayoutAttributeCenterX = 9
NSLayoutAttributeCenterY = 10
NSLayoutAttributeBaseline = 11
NSLayoutAttributeLastBaseline = NSLayoutAttributeBaseline
# NSLayoutAttributeFirstBaseline = 12

NSLayoutAttributeNotAnAttribute = 0

NSLayoutFormatAlignAllLeft = (1 << NSLayoutAttributeLeft)
NSLayoutFormatAlignAllRight = (1 << NSLayoutAttributeRight)
NSLayoutFormatAlignAllTop = (1 << NSLayoutAttributeTop)
NSLayoutFormatAlignAllBottom = (1 << NSLayoutAttributeBottom)
NSLayoutFormatAlignAllLeading = (1 << NSLayoutAttributeLeading)
NSLayoutFormatAlignAllTrailing = (1 << NSLayoutAttributeTrailing)
NSLayoutFormatAlignAllCenterX = (1 << NSLayoutAttributeCenterX)
NSLayoutFormatAlignAllCenterY = (1 << NSLayoutAttributeCenterY)
NSLayoutFormatAlignAllBaseline = (1 << NSLayoutAttributeBaseline)
NSLayoutFormatAlignAllLastBaseline = NSLayoutFormatAlignAllBaseline
# NSLayoutFormatAlignAllFirstBaseline = (1 << NSLayoutAttributeFirstBaseline)

NSLayoutFormatAlignmentMask = 0xFFFF

NSLayoutFormatDirectionLeadingToTrailing = 0 << 16
NSLayoutFormatDirectionLeftToRight = 1 << 16
NSLayoutFormatDirectionRightToLeft = 2 << 16

NSLayoutFormatDirectionMask = 0x3 << 16

UILayoutPriorityRequired = 1000
UILayoutPriorityDefaultHigh = 750
UILayoutPriorityDefaultLow = 250
UILayoutPriorityFittingSizeLevel = 50
