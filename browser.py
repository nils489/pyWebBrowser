#!/usr/bin/env python

from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebKit import QWebSettings
from pWB_shortcuts import pWB_shortcuts
from pWB_settings import pWB_settings
import subprocess
import sys
import os

app = QApplication(sys.argv)

renderer = QWebView()
renderer.show()
if len(sys.argv) > 1:
    if sys.argv[1]:
        initial_url=sys.argv[1]
        renderer.setUrl(QUrl.fromUserInput(initial_url))

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

def title_updated():
    renderer.setWindowTitle(renderer.title())

def create_new_window(urlstring):
    subprocess.run(["python",os.path.realpath(__file__),urlstring])

# page settings
p_settings = pWB_settings(renderer.page())

# renderer actions
sc = pWB_shortcuts(renderer)
sc.back_sc.activated.connect(lambda: renderer.triggerPageAction(QWebPage.Back))
sc.reload_sc.activated.connect(lambda: renderer.triggerPageAction(QWebPage.Reload))
sc.urld_sc.activated.connect(lambda: url_input_dialog())
sc.search_sc.activated.connect(lambda: search_page_input_dialog())
sc.disable_scripts_sc.activated.connect(lambda:
                                        p_settings.ps.setAttribute(QWebSettings.JavascriptEnabled,False))
sc.enable_scripts_sc.activated.connect(lambda:
                                       p_settings.ps.setAttribute(QWebSettings.JavascriptEnabled,True))
renderer.pageAction(QWebPage.OpenLinkInNewWindow).triggered.connect(lambda:
                                                             create_new_window("blog.fefe.de"))

# update view
renderer.titleChanged.connect(lambda: title_updated())

app.exec()

