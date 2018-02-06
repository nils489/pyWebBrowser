#!/usr/bin/env python

from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QShortcut, QInputDialog
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtGui import QKeySequence
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

# keyboard shortcuts
back_sk = QShortcut(QKeySequence(app.tr("Ctrl+H")),renderer)
reload_sk = QShortcut(QKeySequence(app.tr("F5")),renderer)
urld_sk = QShortcut(QKeySequence(app.tr("Ctrl+G")),renderer)
search_sk = QShortcut(QKeySequence(app.tr("/")),renderer)
disable_scripts_sk = QShortcut(QKeySequence(app.tr("Ctrl+S")),renderer)
enable_scripts_sk = QShortcut(QKeySequence(app.tr("Ctrl+Shift+S")),renderer)

# renderer actions
back_sk.activated.connect(lambda: renderer.triggerPageAction(QWebPage.Back))
reload_sk.activated.connect(lambda: renderer.triggerPageAction(QWebPage.Reload))
urld_sk.activated.connect(lambda: url_input_dialog())
search_sk.activated.connect(lambda: search_page_input_dialog())
disable_scripts_sk.activated.connect(lambda: disable_javascript(p_settings))
enable_scripts_sk.activated.connect(lambda: enable_javascript(p_settings))

# page settings
p_settings = renderer.page().settings()
# disable javascript at startup (default behaviour)
disable_javascript(p_settings)
p_settings.setAttribute(QWebSettings.XSSAuditingEnabled, True)

# update view
renderer.urlChanged.connect(lambda: url_updated())

app.exec()

