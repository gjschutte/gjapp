from flask import Blueprint, render_template, redirect, session, url_for, request
from app import db
from app.models import Spreuk, Domein
from flask.ext import menu
from .weather_request import req_weather, req_longterm, prep_chart, req_5days, prep_chart_5d

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

mod3 = Blueprint(
	'days',
	__name__,
	template_folder='templates',
	url_prefix='/weather/days')

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
	w_forecast = req_longterm ()
	
	# Prepare the chart
	temp_chart, rain_chart = prep_chart(w_forecast)

	return render_template('forecast.html',
							title='Weather forecast',
							w_forecast = w_forecast,
							temp_chart = temp_chart,
							rain_chart = rain_chart)

@mod3.route('/')
@menu.register_menu(mod3, '.days', '5 Days', order=5)
def days():
	#get the weather forecast
	w_forecast = req_5days ()
	
	# Prepare the chart
	temp_chart, rain_chart = prep_chart_5d (w_forecast)

	return render_template('days.html',
							title='5 days weather forecast',
							w_forecast = w_forecast,
							temp_chart = temp_chart,
							rain_chart = rain_chart)
