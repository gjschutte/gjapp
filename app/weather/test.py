#!flask/bin/python
import os
import unittest

from config import basedir
from .weather_request import *

class TestCase(unittest.TestCase):
		
	# testing weather_request functions
	
	def test_calc_wind_direction(self):
		assert calc_wind_direction(0) == 'North'
		assert calc_wind_direction(10) == 'North'
		assert calc_wind_direction(359) == 'North - Northwest'
		
	def test_req_weather(self):
		result = req_weather()
		self.assertEqual(result['name'], 'Apeldoorn')
		
		
if __name__ == '__main__':
	unittest.main()
