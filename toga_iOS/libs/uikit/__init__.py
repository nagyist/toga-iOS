from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from ctypes import util, cdll, c_char_p, c_int, c_void_p, POINTER

from rubicon.objc import ObjCClass

from .nslayoutconstraint import *   # noqa
from .nsparagraphstyle import *     # noqa
from .nstext import *               # noqa
from .uicontrol import *            # noqa
from .uigeometry import *           # noqa
from .uitableviewcell import *      # noqa
from .uitextfield import *          # noqa
from .uiview import *               # noqa


_uikit = cdll.LoadLibrary(util.find_library('UIKit'))
_uikit.UIApplicationMain.restype = c_int
_uikit.UIApplicationMain.argtypes = [
    c_int, POINTER(c_char_p), c_void_p, c_void_p,
]

UIButton = ObjCClass('UIButton')
UIColor = ObjCClass('UIColor')
UIImage = ObjCClass('UIImage')
UIImageView = ObjCClass('UIImageView')
UILabel = ObjCClass('UILabel')
UINavigationController = ObjCClass('UINavigationController')
UIResponder = ObjCClass('UIResponder')
UIScreen = ObjCClass('UIScreen')
UIScrollView = ObjCClass('UIScrollView')
UITabBarController = ObjCClass('UITabBarController')
UITableView = ObjCClass('UITableView')
UIViewController = ObjCClass('UIViewController')
UIWebView = ObjCClass('UIWebView')
UIWindow = ObjCClass('UIWindow')
