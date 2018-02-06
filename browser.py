#!/usr/bin/env python

from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebKit import QWebSettings
from shortcuts import pWB_shortcuts
import sys

app = QApplication(sys.argv)

renderer = QWebView()
renderer.show()

def url_input_dialog():
    url_tuple = QInputDialog.getText(renderer,
                                     app.tr("URL-Dialog"),
                                     app.tr("URL:"),
                                     text=renderer.url().toDisplayString())
    if not url_tuple[0]:
        url_string = renderer.url().toDisplayString()
        print("URL-String empty")
    else:
        url_string = url_tuple[0]
        print("URL-String: "+url_string)
    renderer.setUrl(QUrl.fromUserInput(url_string))

def search_page_input_dialog():
    search_tuple = QInputDialog.getText(renderer,
                                        app.tr("Search page"),
                                        app.tr("search: "))
    renderer.findText(search_tuple[0])

def url_updated():
    renderer.setWindowTitle(renderer.url().toDisplayString())

def disable_javascript(sttngs):
    sttngs.setAttribute(QWebSettings.JavascriptEnabled, False)

def enable_javascript(sttngs):
    sttngs.setAttribute(QWebSettings.JavascriptEnabled, True)

# renderer actions
sc = pWB_shortcuts(renderer)
sc.back_sc.activated.connect(lambda: renderer.triggerPageAction(QWebPage.Back))
sc.reload_sc.activated.connect(lambda: renderer.triggerPageAction(QWebPage.Reload))
sc.urld_sc.activated.connect(lambda: url_input_dialog())
sc.search_sc.activated.connect(lambda: search_page_input_dialog())
sc.disable_scripts_sc.activated.connect(lambda: disable_javascript(p_settings))
sc.enable_scripts_sc.activated.connect(lambda: enable_javascript(p_settings))

# page settings
p_settings = renderer.page().settings()
# disable javascript at startup (default behaviour)
disable_javascript(p_settings)
p_settings.setAttribute(QWebSettings.XSSAuditingEnabled, True)

# update view
renderer.urlChanged.connect(lambda: url_updated())

app.exec()

