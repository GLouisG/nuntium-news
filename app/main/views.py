from flask import render_template,url_for
from . import main
from ..requests import find_articles, find_sources

@main.route('/')
def index():
  the_sources = find_sources('sourceinfo')
  title = 'News Sources'
  return render_template('index.html', title=title, sourceinfo=the_sources)
@main.route('/newspieces/<source_id>')
def newspieces(source_id):
  the_articles = find_articles(source_id)
  title = f'From {source_id}'
  return render_template('newspieces.html', title=title, les_articles=the_articles)
