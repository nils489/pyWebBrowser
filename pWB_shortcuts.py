#!/usr/bin/env python

from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

class pWB_shortcuts:
    'Class that holds all keyboard shortcuts for pWB'
    def __init__(self,parent):
        self.back_sc = QShortcut(QKeySequence(parent.tr("Ctrl+H")),parent)
        self.reload_sc = QShortcut(QKeySequence(parent.tr("F5")),parent)
        self.urld_sc = QShortcut(QKeySequence(parent.tr("Ctrl+G")),parent)
        self.search_sc = QShortcut(QKeySequence(parent.tr("/")),parent)
        self.disable_scripts_sc = QShortcut(QKeySequence(parent.tr("Ctrl+S")),
                                       parent)
        self.enable_scripts_sc = QShortcut(QKeySequence(parent.tr("Ctrl+Shift+S")),
                                      parent)
