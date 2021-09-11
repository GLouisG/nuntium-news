from flask import render_template,url_for
from . import main
from ..requests import find_sources

@main.route('/')
def index():
  the_sources = find_sources('sourceinfo')
  title = 'News Sources'
  return render_template('index.html', title=title, sourceinfo=the_sources)

