import urllib.request,json
from .models import Sources

api_key = None
article_base_url = None
sources_base_url = None
def configure_request(app):
  global api_key,article_base_url,sources_base_url
  api_key = app.config['API_KEY']
  article_base_url = app.config['ARTICLE_BASE_URL']
  sources_base_url = app.config['SOURCES_BASE_URL']
  
