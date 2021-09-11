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

def find_sources(info):
  get_sources_url = sources_base_url.format(api_key)
  
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response=json.loads(get_sources_data)

    sources_results = None

    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = process_results(sources_results_list)
  return sources_results
      