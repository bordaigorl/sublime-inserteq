import sublime
import sublime_plugin

from tempfile import mkstemp
import os

import urllib.request as download
from urllib.parse import quote as urlquote
# from urllib.parse import unquote as urlunquote

EMPTYGIF = b"""\
\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\
\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\
\x01\x00\x01\x00\x00\x02\x01\x44\x00\x3b"""


def find_syntax(lang, default=None):
    res = sublime.find_resources("%s.*Language" % lang)
    if res:
        return res[-1]
    else:
        return (default or ("Packages/%s/%s.tmLanguage" % lang))


class InsertEquationCommand(sublime_plugin.TextCommand):

    url = "http://latex.codecogs.com/gif.latex?{query}"

    def get_url(self, query):
        return self.url.format(query=urlquote(query))

    def on_cancel(self):
        self.window.run_command("close")
        os.remove(self.preview_file)

    def to_markdown(self, alt, url):
        for ch in ['\\', '_', '*', '`']:
            alt = alt.replace(ch, "\\"+ch)
        # not storing alt in `alt` attribute since not all markdown converters
        # handle special symbols well in it.
        return '![formula]({url} "{alt}")'.format(alt=alt, url=url)

    def to_html(self, alt, url):
        alt = alt.replace("<", "&lt;")
        alt = alt.replace(">", "&gt;")
        alt = alt.replace("&", "&amp;")
        return '<img alt="{alt}" src="{url}" />'.format(alt=alt, url=url)

    def to_text(self, alt, url):
        return url

    def to_source(self, alt, url):
        return '"%s"' % url

    def on_change(self, txt):
        if self.busy:
            return

        self.busy = True

        def update_preview():
            self.busy = False
            txt = self.input_view.substr(sublime.Region(0, self.input_view.size()))
            print("Previewing %s" % txt)
            url = self.get_url(txt)
            download.urlretrieve(url, self.preview_file)

        sublime.set_timeout_async(update_preview, 10)

    def on_done(self, txt):
        url = self.get_url(txt)
        img = getattr(self, 'to_%s' % self.convert_to, self.to_text)(txt, url)
        self.window.run_command("close")
        self.view.run_command("insert", {"characters": img})
        os.remove(self.preview_file)

    def run(self, e, renderer=None, slurp=True, convert_to="auto"):
        self.busy = False

        if convert_to == "auto":
            syntax = self.view.scope_name(self.view.sel()[0].a).split()[0].split('.')
            if "markdown" in syntax:  # special case
                convert_to = "markdown"
            else:
                convert_to = syntax[min(len(syntax)-1, 1)]
            if not hasattr(self, "to_%s" % convert_to):
                convert_to = syntax[0]
        self.convert_to = convert_to

        if renderer:
            self.url = renderer

        query = ""
        if slurp and self.view.has_non_empty_selection_region():
            query = self.view.substr(self.view.sel()[0])

        self.window = self.view.window()
        _, self.preview_file = mkstemp(suffix=".gif")
        gif = open(self.preview_file, 'wb')
        gif.write(EMPTYGIF)
        gif.close()
        self.preview = self.window.open_file(self.preview_file, sublime.TRANSIENT)
        self.input_view = self.window.show_input_panel(
            "Input LaTeX equation:", query, self.on_done, self.on_change, self.on_cancel)
        self.input_view.set_syntax_file(find_syntax("TeX"))
        self.input_view.settings().set("gutter", False)
