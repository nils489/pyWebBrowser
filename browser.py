#!/usr/bin/env python

from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QShortcut, QInputDialog
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtGui import QKeySequence
import sys

app = QApplication(sys.argv)

renderer = QWebView()
renderer.show()

def url_input_dialog():
    url_tuple = QInputDialog.getText(renderer,
                                      app.tr("URL-Dialog"),
                                      app.tr("URL:"))
    if not url_tuple[0]:
        url_string = renderer.url().toDisplayString()
        print("URL-String empty")
    else:
        url_string = url_tuple[0]
        print("URL-String: "+url_string)
    renderer.setUrl(QUrl.fromUserInput(url_string))

# keyboard shortcuts
back_sk = QShortcut(QKeySequence(app.tr("Ctrl+H")),renderer)
reload_sk = QShortcut(QKeySequence(app.tr("F5")),renderer)
urld_sk = QShortcut(QKeySequence(app.tr("Ctrl+G")),renderer)

# renderer actions
back_sk.activated.connect(lambda: renderer.triggerPageAction(QWebPage.Back))
reload_sk.activated.connect(lambda: renderer.triggerPageAction(QWebPage.Reload))
urld_sk.activated.connect(lambda: url_input_dialog())

app.exec()

