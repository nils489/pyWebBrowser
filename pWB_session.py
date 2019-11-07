#!/usr/bin/env python


class pWB_session:
    'holds the state of the current pyWebBrower session'
    def __init__(self, views):
        self.views = views
        self.active_view = self.views[0]

    def set_view_active(self, ind):
        self.active_view = self.views[ind]

    #def set_view_active(self, view):
    #    self.active_view = view
