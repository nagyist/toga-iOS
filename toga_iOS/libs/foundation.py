from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)
from ctypes import cdll, c_bool, util

from rubicon.objc import ObjCClass, NSPoint, NSRect


foundation = cdll.LoadLibrary(util.find_library('Foundation'))
foundation.NSMouseInRect.restype = c_bool
foundation.NSMouseInRect.argtypes = [NSPoint, NSRect, c_bool]

NSArray = ObjCClass('NSArray')
NSData = ObjCClass('NSData')
NSMutableArray = ObjCClass('NSMutableArray')
NSObject = ObjCClass('NSObject')
NSURL = ObjCClass('NSURL')
NSURLRequest = ObjCClass('NSURLRequest')
