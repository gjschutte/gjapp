#!/usr/bin/env python
# -*- coding: utf -8 -*-
#
# location.py
# 
#  Copyright 2015 schutte <schutte@debian>
#  09-10-2015
#

import requests
import geocoder
from geopy.geocoders import Nominatim


def check_location(place):
	# determine longitude and langitude for a given place

	geolocator = Nominatim()
	loc = geolocator.geocode(place)
	
	return (loc.address, loc.latitude, loc.longitude)
	
def get_location_by_ip():
	# Determine location based on the ip address
	# Not working!!!
	
	place = geocoder.ip('me')
	print (place)
	#result = geocoder.reverse(place.latlng)
	#result = result.json
	# print (result)
	
	return "Apeldoorn" 

def main():
	
	place = get_location_by_ip()
	print (place)
	# location = check_location ("Apeldoorn")
	
	return 0


if __name__ == '__main__':
	main()
