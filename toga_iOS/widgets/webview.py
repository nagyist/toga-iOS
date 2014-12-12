from __future__ import (
    absolute_import, division, print_function, unicode_literals,
)

from rubicon.objc import objc_method

from ..libs import NSURL, NSURLRequest, UIWebView
from .base import Widget


class WebViewImpl(UIWebView):
    @objc_method('v@')
    def setURL_(self, url):
        request = NSURLRequest.alloc().initWithURL_(url)
        self.loadRequest_(request)


class WebView(Widget):
    def __init__(self, url=None):
        super(WebView, self).__init__()
        self.startup()
        self.url = url

    def startup(self):
        self._impl = WebViewImpl.alloc().init()
        self._impl.setDelegate_(self._impl)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        if value:
            url = NSURL.URLWithString_(value)
            self._impl.setURL_(url)
