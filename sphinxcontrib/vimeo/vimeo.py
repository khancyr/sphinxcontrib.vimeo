#-*- coding:utf-8 -*-

import re

from docutils import nodes
from docutils.parsers import rst


class vimeo(nodes.General, nodes.Element):
    pass


def visit(self, node):

    video_id = node.video_id
    height = node.height
    width = node.width

    tag = (
        '<iframe src="https://player.vimeo.com/video/{video_id}"'
        'width="{width}" height="{height}" frameborder="0" '
        'webkitallowfullscreen mozallowfullscreen allowfullscreen>'
        '</iframe>').format(
            video_id=video_id,
            width=width,
            height=height)

    self.body.append(tag)


def depart(self, node):
    pass


class VimeoDirective(rst.Directive):

    name = 'vimeo'
    node_class = vimeo

    has_content = False
    required_arguments = 1
    optional_arguments = 2
    final_argument_whitespace = False
    option_spec = {
        'height': int,
        'width': int,
    }

    def run(self):
        node = self.node_class()
        arg = self.arguments[0]
        if re.match('^http[s]?://', arg):
            # URL expected format: https://vimeo.com/40045057
            node.video_id = arg.split('/')[-1]
        else:
            node.video_id = arg

        node.height = self.options['height']
        node.width = self.options['width']

        return [node]
