from flask import Flask
from config import config_options
# from flask_bootstrap import Bootstrap




def create_app(config_name):
  app = Flask(__name__, template_folder='templates')
  app.config.from_object(config_options[config_name])


  #register the blueprint
  from .main import Blueprint as main_blueprint
  app.register_blueprint(main_blueprint)

  #REMEMBER TO UNCOMMENT ME

  # bootstrap.init_app(app)



 


  # # setting config
  from .requests import configure_request
  configure_request(app)



  return app