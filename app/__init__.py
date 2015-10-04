import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.menu import current_menu
from flask.ext import menu

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
menu.Menu(app=app)

# Import modules
# from .home import home
from app.home.views import mod as homeModule
from app.analyse.views import mod as analyseModule
from app.beheer.views import mod as beheerModule
from app.weather.views import mod as weatherModule
from app.weather.views import mod2 as forecastModule
from app.weather.views import mod3 as daysModule

if not app.debug and os.environ.get('HEROKU') is None:
	import logging
	from logging.handlers import RotatingFileHandler
	file_handler = RotatingFileHandler('tmp/gjapp.log', 'a', 1 * 1024 * 1024, 10)
	file_handler.setLevel(logging.INFO)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	app.logger.addHandler(file_handler)
	app.logger.setLevel(logging.INFO)
	app.logger.info('gjapp startup')
	
if os.environ.get('HEROKU') is not None:
	import logging
	stream_handler = logging.StreamHandler()
	app.logger.addHandler(stream_handler)
	app.logger.setLevel(logging.INFO)
	app.logger.info('gjapp startup')

from app import models

# Register the blueprints
app.register_blueprint(homeModule)
app.register_blueprint(analyseModule)
app.register_blueprint(beheerModule)
app.register_blueprint(weatherModule)
app.register_blueprint(forecastModule)
app.register_blueprint(daysModule)
