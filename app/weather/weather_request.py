#!/usr/bin/env python
# -*- coding: utf -8 -*-
#
# weather_request.py
# 
#  Copyright 2015 schutte <schutte@debian>
#  05-07-2015
#

import requests

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
	return wind_table[i]

def make_rainfall (r):
	# Determine rain or snow, add right text
	if ('rain' in r):
		text = str(r['rain']['1h']) + 'mm per hour'
	elif ('snow' in r):
		text = str(r['snow']['1h']) + 'mm snow per hour'
	else:
		text = 'No rainfall'
	
	return text

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

	return result
	
def main():
	
	weer = req_weather()
	
	return 0

if __name__ == '__main__':
	main()
