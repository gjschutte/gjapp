#!/usr/bin/env python
# -*- coding: utf -8 -*-
#
# weather_request.py
# 
#  Copyright 2015 schutte <schutte@debian>
#  05-07-2015
#

import requests
from datetime import datetime
from time import strftime
from pprint import pprint

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
	
def make_date (timestamp):
	# Based on the timestamp, give the date
	# Format: ddd, dd mon yyyy
	fmt = "%a, %d %b %Y"
	datum = datetime.fromtimestamp(timestamp)
	datum = (datum.strftime(fmt))

	return datum

def req_weather ():
	# call openweathermap
	url = 'http://api.openweathermap.org/data/2.5/weather'

	params = dict(
		q='Apeldoorn',
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


def req_forecast ():
	# call openweathermap
	url = 'http://api.openweathermap.org/data/2.5/forecast'

	params = dict(
		q='Apeldoorn',
		APPID='e23b02c9fd9a90ccb44df46cb9af0757',
		units='metric'
	)

	r = requests.get(url=url, params=params)
	result = r.json()
	
	# Calculate the averages per day
	av_p_day = calc_average_per_day (result)

	return (result, av_p_day)

def req_longterm ():
	# max 16 days forecast, totals per day
	# call openweathermap
	url = 'http://api.openweathermap.org/data/2.5/forecast/daily'

	params = dict(
		q='Apeldoorn',
		APPID='e23b02c9fd9a90ccb44df46cb9af0757',
		units='metric',
		cnt='14'
	)

	r = requests.get(url=url, params=params)
	result = r.json()
	
	# Change timestamp to readable date
	# Round the min and max temperature
	for row in result['list']:
		date_txt = make_date(row['dt'])
		row['date_txt'] = date_txt
		
		max_round = round(row['temp']['max'])
		row['temp']['max_round'] = max_round
		min_round = round(row['temp']['min'])
		row['temp']['min_round'] = min_round

		
	return result
	
	
def main():
	
	result = req_longterm()
	pprint (result)
	
	return 0

if __name__ == '__main__':
	main()
