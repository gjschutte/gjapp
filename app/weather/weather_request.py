#!/usr/bin/env python
# -*- coding: utf -8 -*-
#
# weather_request.py
# 
#  Copyright 2015 schutte <schutte@debian>
#  05-07-2015
#

import requests, pygal
from datetime import datetime
from time import strftime
from pprint import pprint
from pygal.style import DefaultStyle

def calc_wind (wind_ms):
	# Calculate beaufort value based on miles per second
	wind_table = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6]

	wind_beaufort = 12
	for index in range(len(wind_table)):
		if (wind_ms <= wind_table[index]):
			wind_beaufort = index
			break

	return wind_beaufort

def calc_wind_direction(degrees):
	# Define wind direction based on degrees
	wind_table = ['North',
					'North - northeast',
					'Northeast',
					'East - northeast',
					'East',
					'East - southeast',
					'Southeast',
					'South - southeast',
					'South',
					'South - southwest',
					'Southwest',
					'West - Southwest',
					'West',
					'West - Northwest',
					'Northwest',
					'North - Northwest']
					
	i = round(degrees / 22.5)
	if (i == 16):
		i = 15
		
	return wind_table[i]

def make_rainfall (r):
	# Determine rain or snow, add right text
	if (('rain' in r) and ('1h' in r)):
		text = str(r['rain']['1h']) + 'mm per hour'
	elif (('snow' in r) and ('1h' in r)):
		text = str(r['snow']['1h']) + 'mm snow per hour'
	else:
		text = 'No rainfall'
	
	return text
	
def make_date (timestamp, form):
	# Based on the timestamp, give the date
	# Format 1: ddd, dd mon yyyy
	# Format 2: dd mm
	# Format 3: hh
	# Format 4: ddd
	if (form == 1):
		fmt = "%a, %d %b %Y"
	else:
		if (form == 2):
			fmt = "%e-%m"
		else:
			if (form == 3):
				fmt = "%H"
			else:
				fmt = "%a"
	
	datum = datetime.fromtimestamp(timestamp)
	datum = (datum.strftime(fmt))

	return datum

def req_weather (latitude, longitude):
	# call openweathermap
	url = 'http://api.openweathermap.org/data/2.5/weather'

	params = dict(
		#q='Apeldoorn',
		lat=latitude,
		lon=longitude,
		APPID='e23b02c9fd9a90ccb44df46cb9af0757',
		units='metric'
	)

	r = requests.get(url=url, params=params)
	result = r.json()


	# Calculate wind in beaufort
	wind_kr = calc_wind(result['wind']['speed'])
	result['wind']['beaufort'] = wind_kr

	# Calculate wind direction
	wind_dir = calc_wind_direction(result['wind']['deg'])
	result['wind']['dir'] = wind_dir
	
	# Calculate rainfall
	rainfall = make_rainfall(result)
	result['rainfall'] = rainfall
	
	return result

def calc_average_per_day (result):
	# calculate the averages per day
	# return a new list with results
	first = 'Y'
	list_dates = []
	for row in result['list']:
		if (first == 'Y'):
			w_day = {'date': row['dt_txt'][:10], 'max_temp' : row['main']['temp'], 'min_temp' : row['main']['temp']}
			first = 'N'
		
		if (row['dt_txt'][:10] != w_day['date']):
			#new day, save the data
			list_dates.append (w_day)
			w_day = {'date': row['dt_txt'][:10], 'max_temp' : row['main']['temp'], 'min_temp' : row['main']['temp']}
		else :
			if (row['main']['temp'] > w_day['max_temp']):
				w_day['max_temp'] = row['main']['temp']
			if (row['main']['temp'] < w_day['min_temp']):
				w_day['min_temp'] = row['main']['temp']
	
	list_dates.append (w_day)
	
	return list_dates

def req_5days (latitude, longitude):
	# call openweathermap, 5 days-3 hours forecast
	url = 'http://api.openweathermap.org/data/2.5/forecast'

	params = dict(
		# q='Apeldoorn',
		lat = latitude,
		lon = longitude,
		APPID='e23b02c9fd9a90ccb44df46cb9af0757',
		units='metric'
	)

	r = requests.get(url=url, params=params)
	result = r.json()
	
	return result

def prep_chart_5d (result) :
	list_times = []
	list_temp = []
	list_rain = []
	last_date = ''

	for row in result['list']:
		# Make this lists with times, temperatures, rain
		date_short = make_date(row['dt'], 4)
		if (date_short != last_date):
			list_times.append(date_short)
			last_date = date_short
		else :
			list_times.append('')
		list_temp.append(row['main']['temp'])
		if ('rain' in row):
			try:
				list_rain.append(row['rain']['3h'])
			except:
				list_rain.append(0)
		else :
			list_rain.append(0)
		
	#create the temperature chart
	title = 'Temperature: 5 days forecast'
	temp_chart = pygal.Line( fill = True,
							width = 700, height = 400,
							x_label_rotation = 45,
							# x_labels_major_count = 3,
							# show_minor_x_labels=False,
							explicit_size=True,
							title = title,
							x_title = 'Time',
							style=DefaultStyle,
							disable_xml_declaration=True)
	temp_chart.x_labels = list_times
	temp_chart.add('Temperature', list_temp)
	
	# create the rain chart
	title = 'Rainfall: 5 days forecast, mm rain per 3 hours'
	rain_chart = pygal.Bar( fill = True,
							width = 700, height = 400,
							explicit_size = True,
							title = title,
							x_title = 'Time',
							style = DefaultStyle,
							disable_xml_declaration = True)
	rain_chart.x_labels = list_times
	rain_chart.add('Rain', list_rain)
	
	return (temp_chart, rain_chart)
	

def req_longterm (latitude, longitude):
	# max 16 days forecast, totals per day
	# call openweathermap
	url = 'http://api.openweathermap.org/data/2.5/forecast/daily'

	params = dict(
		# q='Apeldoorn',
		lat = latitude, 
		lon = longitude,
		APPID='e23b02c9fd9a90ccb44df46cb9af0757',
		units='metric',
		cnt='14'
	)

	r = requests.get(url=url, params=params)
	result = r.json()
	
	# Change timestamp to readable date
	# Round the min and max temperature
	for row in result['list']:
		date_txt = make_date(row['dt'], 1)
		row['date_txt'] = date_txt
		
		max_round = round(row['temp']['max'])
		row['temp']['max_round'] = max_round
		min_round = round(row['temp']['min'])
		row['temp']['min_round'] = min_round

		# Calculate wind in beaufort
		wind_kr = calc_wind(row['speed'])
		row['beaufort'] = wind_kr

		# Calculate wind direction
		wind_dir = calc_wind_direction(row['deg'])
		row['dir'] = wind_dir
		
	return result
	
def prep_chart (result):
	list_dates = []
	list_max = []
	list_min = []
	list_rain = []

	for row in result['list']:
		# Make this lists with dates, temperatures, rain
		date_short = make_date(row['dt'], 2)
		list_dates.append(date_short)
		list_max.append(row['temp']['max'])
		list_min.append(row['temp']['min'])
		if ('rain' in row):
			list_rain.append(row['rain'])
		else :
			list_rain.append(0)
		
	#create the temperature chart
	title = '14-days temperature'
	temp_chart = pygal.Line( fill = True,
							width = 500, height = 400,
							explicit_size=True,
							title = title,
							style=DefaultStyle,
							disable_xml_declaration=True)
	temp_chart.x_labels = list_dates
	temp_chart.add('Maximum', list_max)
	temp_chart.add('Minimum', list_min)
	
	# create the rain chart
	title = 'Rain (mm per day)'
	rain_chart = pygal.Bar( fill = True,
							width = 500, height = 400,
							explicit_size = True,
							title = title,
							style = DefaultStyle,
							disable_xml_declaration = True)
	rain_chart.x_labels = list_dates
	rain_chart.add('Rain', list_rain)
	
	return (temp_chart, rain_chart)
	
def main():
	
	result = req_5days()
#	bar_char = prep_chart(result)
	pprint (result)
	
	return 0

if __name__ == '__main__':
	main()
