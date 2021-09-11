from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
  app = Flask(__name__,template_folder='templates')
  app.config.from_object(config_options[config_name])

  bootstrap.init_app(app)
  #register the blueprint
  from .main import main as mains_blueprint
  app.register_blueprint(mains_blueprint)



  



 


  # # setting config
  from .requests import configure_request
  configure_request(app)



  return app