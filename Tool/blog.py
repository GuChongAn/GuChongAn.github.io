import re
import os

import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


class myBlogRenderer(mistune.HTMLRenderer):
    # code highlight
    def block_code(self, code, info=None):
        if info:
            lexer = get_lexer_by_name(info, stripall=True)
            formatter = HtmlFormatter()
            return highlight(code, lexer, formatter)
        return '<pre><code>' + mistune.escpae(code) + '</code></pre>'

    def inline_math(self, text):
        return '<span class="math">$' + mistune.escape(text) + '$</span>'


class Blog():
    def __init__(self, path):
        self.path = path
        self.name, _ = os.path.splitext(os.path.basename(path))

        with open(path, 'r', encoding='utf-8') as f:
            md = f.read()

        markdown = mistune.create_markdown(renderer=myBlogRenderer(), plugins=['math', 'table'])
        self.info, md = self.getBlogInfo(md)
        self.blog = markdown(md)

    # get blog information
    def getBlogInfo(self, blog):
        # process markdown
        pattern = r'---(.*?)---'
        info = re.findall(pattern, blog, re.DOTALL)[0]
        blog = re.sub(r'---' + re.escape(info) + r'---', '', blog, count=1)

        # set file information
        infoMap = {}
        lines = info.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        info = '\n'.join(non_empty_lines)
        lines = info.strip().split('\n')
        for line in lines:
            key, value = line.strip().split(':')
            infoMap[key.strip()] = value.strip()

        return infoMap, blog
