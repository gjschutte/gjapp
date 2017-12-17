from flask import Blueprint, render_template, redirect, session, url_for, request, session, flash
from app import db
from app.models import Spreuk, Domein
from flask.ext import menu
from .weather_request import req_weather, req_longterm, prep_chart, req_5days, prep_chart_5d
from .place_form import PlaceForm
from .location import get_location_by_ip, check_location

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

@mod.route('/', methods = ['GET', 'POST'])
@menu.register_menu(mod, '.weather', 'Weather', order=3)
def weather():
	# Form to ask for the location
	form = PlaceForm ()

	if form.validate_on_submit():
		# Check the location
		location, latitude, longitude = check_location(form.City.data)
		form.City.data = location
		session['city'] = location
		session['latitude'] = latitude
		session['longitude'] = longitude
		return redirect(url_for('weather.weather'))
			
	if 'city' not in session:
		# No place defined yet, get default place by IP
		place = "Amsterdam" 
		form.City.data = "Amsterdam" 
		# get the long and lat for the location
		location, latitude, longitude = check_location(form.City.data)
		session['city'] = location
		session['latitude'] = latitude
		session['longitude'] = longitude
	else:
		place = session['city']
		latitude = session['latitude']
		longitude = session['longitude']
		
	# get the actual weather
	w_forecast = req_weather(latitude, longitude)
	
	return render_template('weather.html',
							title='Actual weather',
							form = form,
							w_forecast = w_forecast)
							
@mod2.route('/', methods = ['GET', 'POST'])
# @menu.register_menu(mod2, '.forecast', 'Weather Forecast', order=4)
def forecast():
	# Form to ask for the location
	form = PlaceForm ()

	if form.validate_on_submit():
		# Check the location
		location, latitude, longitude = check_location(form.City.data)
		form.City.data = location
		session['city'] = location
		session['latitude'] = latitude
		session['longitude'] = longitude
		return redirect(url_for('forecast.forecast'))
			
	if 'city' not in session:
		# No place defined yet, get default place by IP
		place = get_location_by_ip()
		form.City.data = place
		# get the long and lat for the location
		location, latitude, longitude = check_location(form.City.data)
		session['city'] = location
		session['latitude'] = latitude
		session['longitude'] = longitude
	else:
		place = session['city']
		latitude = session['latitude']
		longitude = session['longitude']
		


	#get the weather forecast
	w_forecast = req_longterm (latitude, longitude)
	
	# Prepare the chart
	temp_chart, rain_chart = prep_chart(w_forecast)

	return render_template('forecast.html',
							title='Weather forecast',
							form = form,
							w_forecast = w_forecast,
							temp_chart = temp_chart,
							rain_chart = rain_chart)

@mod3.route('/', methods = ['GET', 'POST'])
# @menu.register_menu(mod3, '.days', '5 Days', order=5)
def days():
	# Form to ask for the location
	form = PlaceForm ()

	if form.validate_on_submit():
		# Check the location
		location, latitude, longitude = check_location(form.City.data)
		form.City.data = location
		session['city'] = location
		session['latitude'] = latitude
		session['longitude'] = longitude
		return redirect(url_for('days.days'))
			
	if 'city' not in session:
		# No place defined yet, get default place by IP
		place = get_location_by_ip()
		form.City.data = place
		# get the long and lat for the location
		location, latitude, longitude = check_location(form.City.data)
		session['city'] = location
		session['latitude'] = latitude
		session['longitude'] = longitude
	else:
		place = session['city']
		latitude = session['latitude']
		longitude = session['longitude']

	#get the weather forecast
	w_forecast = req_5days (latitude, longitude)
	
	# Prepare the chart
	temp_chart, rain_chart = prep_chart_5d (w_forecast)

	return render_template('days.html',
							title='5 days weather forecast',
							form = form,
							w_forecast = w_forecast,
							temp_chart = temp_chart,
							rain_chart = rain_chart)
