#-*- coding:utf-8 -*-

__version__ = '0.0.1'


def setup(app):
    from . import vimeo
    app.add_node(vimeo.vimeo, html=(vimeo.visit, vimeo.depart))
    app.add_directive('vimeo', vimeo.VimeoDirective)
