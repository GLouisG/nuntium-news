import os

class Config:
  ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&language=en&apiKey={}'
  SOURCES_BASE_URL='https://newsapi.org/v2/top-headlines/sources?language=en&apiKey={}'
  API_KEY=os.environ.get('API_KEY')
class ProdConfig(Config) :


  pass 
class DevConfig(Config):
  '''
    Development  configuration child class of Config

    Args:
    Config: The parent configuration class with General configuration settings
  
  '''

  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 