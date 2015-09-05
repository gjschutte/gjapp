from flask import Blueprint, render_template, redirect, session, url_for, request
from app import db
from app.models import Spreuk, Domein
from flask.ext import menu
from .weather_request import req_weather

mod = Blueprint(
			'weather', 
			__name__, 
			template_folder='templates',
			url_prefix='/weather')
			
mod2 = Blueprint(
	'forecast',
	__name__,
	template_folder='templates',
	url_prefix='/weather/forecast')

@mod.route('/')
@menu.register_menu(mod, '.weather', 'Weather', order=3)
def weather():
	# get the actual weather
	w_forecast = req_weather()
	
	return render_template('weather.html',
							title='Actual weather',
							w_forecast = w_forecast)
							
@mod2.route('/')
@menu.register_menu(mod2, '.forecast', 'Weather Forecast', order=4)
def forecast():
	#get the weather forecast
	w_forecast = req_weather()

	return render_template('forecast.html',
							title='Weather forecast',
							w_forecast = w_forecast)
