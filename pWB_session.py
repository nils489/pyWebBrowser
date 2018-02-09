#!/usr/bin/env python

from PyQt5.QtWebKitWidgets import QWebView,QWebPage

class pWB_session:
    'holds the state of the current pyWebBrower session'
    def __init__(self,views):
        self.views = views
        self.active_view = self.views[0]

    def set_view_active(id):
        self.active_view = self.views[id]

    def set_view_active(view):
        self.active_view = view
