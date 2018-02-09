#!/usr/bin/env python

from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebKit import QWebSettings
from pWB_shortcuts import pWB_shortcuts
from pWB_settings import pWB_settings
from pWB_session import pWB_session
import sys
import os

app = QApplication(sys.argv)

session = pWB_session([QWebView()])
session.active_view.show()

if len(sys.argv) > 1:
    if sys.argv[1]:
        initial_url=sys.argv[1]
        session.active_view.setUrl(QUrl.fromUserInput(initial_url))

def url_input_dialog():
    url_tuple = QInputDialog.getText(session.active_view,
                                     app.tr("URL-Dialog"),
                                     app.tr("URL:"),
                                     text=session.active_view.url().toDisplayString())
    if not url_tuple[0]:
        url_string = session.active_view.url().toDisplayString()
        print("URL-String empty")
    else:
        url_string = url_tuple[0]
        print("URL-String: "+url_string)
    session.active_view.setUrl(QUrl.fromUserInput(url_string))

def search_page_input_dialog():
    search_tuple = QInputDialog.getText(session.active_view,
                                        app.tr("Search page"),
                                        app.tr("search: "))
    session.active_view.findText(search_tuple[0])

def title_updated():
    session.active_view.setWindowTitle(session.active_view.title())

def set_current_link(url):
    print(url)
    current_link = url

# page settings
p_settings = pWB_settings(session.active_view.page())

# active_view actions
sc = pWB_shortcuts(session.active_view)
sc.back_sc.activated.connect(lambda: session.active_view.triggerPageAction(QWebPage.Back))
sc.reload_sc.activated.connect(lambda: session.active_view.triggerPageAction(QWebPage.Reload))
sc.urld_sc.activated.connect(lambda: url_input_dialog())
sc.search_sc.activated.connect(lambda: search_page_input_dialog())
sc.disable_scripts_sc.activated.connect(lambda:
                                        p_settings.ps.setAttribute(QWebSettings.JavascriptEnabled,False))
sc.enable_scripts_sc.activated.connect(lambda:
                                       p_settings.ps.setAttribute(QWebSettings.JavascriptEnabled,True))

# update view
session.active_view.titleChanged.connect(lambda: title_updated())

app.exec()

