#!/usr/bin/env python

from PyQt5.QtWebKit import QWebSettings

class pWB_settings:
    'Class to handle page settings'
    def __init__(self,page):
        self.page = page
        self.ps = self.page.settings()
        # disable javascript at startup (default behaviour)
        self.page.settings().setAttribute(QWebSettings.JavascriptEnabled,False)
        self.page.settings().setAttribute(QWebSettings.XSSAuditingEnabled, True)

