import urllib.request,json
from .models import Articles, Sources

api_key = None
article_base_url = None
sources_base_url = None
def configure_request(app):
  global api_key,article_base_url,sources_base_url
  api_key = app.config['API_KEY']
  article_base_url = app.config['ARTICLE_BASE_URL']
  sources_base_url = app.config['SOURCES_BASE_URL']

def find_sources(info):
  '''
  get json for sources and calls out result processor
  '''
  get_sources_url = sources_base_url.format(api_key)
  
  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response=json.loads(get_sources_data)

    sources_results = None

    if get_sources_response['sources']:
      sources_results_list = get_sources_response['sources']
      sources_results = sources_result_processer(sources_results_list)
  return sources_results
def sources_result_processer(sources_list):
  '''
  sources_list sources_results_list
  '''      
  listed_sources=[]
  for source_item in sources_list:
    id = source_item.get('id')
    name = source_item.get('name')
    source_address = source_item.get('url')

    source_object = Sources(id, name, source_address)
    listed_sources.append(source_object)
  return listed_sources  
def find_articles(source_address):
  '''
  Function to get json response from the url request
  '''
  get_articles_url = article_base_url.format(source_address, api_key)
  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    get_articles_response=json.loads(get_articles_data)

    articles_results = None

    if get_articles_response['articles']:
      articles_results_list = get_articles_response['articles']
      articles_results = articles_result_processer(articles_results_list)
  return articles_results
def articles_result_processer(the_articles_list):  
  '''
  function to process articles results
  the_articles_list is articles_results_list
  '''
  listed_articles=[]
  for article_item in the_articles_list:
    name = article_item.get('name')
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    articleurl = article_item.get('url')
    imageurl = article_item.get('urlToImage')

    article_object = Articles(name, author, description, title, description,articleurl,imageurl)
    listed_articles.append(article_object)
  return listed_articles  