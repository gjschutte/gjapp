#!/usr/bin/env python
# -*- coding: utf -8 -*-
#
# twitter.py
# 
#  Copyright 2016 schutte <schutte@debian>
#  19-03-2016
#

import requests
from requests_oauthlib import OAuth1 # For authentication
from datetime import datetime
from time import strftime
from pprint import pprint
from ttp import ttp
import time

def format_date (tweet_date):
	
	ts = time.strftime('%e %b %Y - %H:%M', time.strptime(tweet_date, '%a %b %d %H:%M:%S +0000 %Y'))
	return ts

def req_twitter (search_items):
	# define twitter_authorizations
	_consumer_key = "axUO19ALyf4XGAjm12BgAwFFx"
	_consumer_secret = "4c4s1OEUBYUNnpcKkAqyhceoEkDn5Et7gfpTo3eBU2sAXCA3EY"
	_key = "219434782-bSCQK2hQD3KAjbWoH8IPIoWvTwXqHZZRnTcfamJk"
	_secret = "qKBldO1TyLeRteUNbsE1m4KKt04MHux8KipripqYsLh4m"
	
	_auth = OAuth1(_consumer_key, _consumer_secret, _key, _secret)
	

	p = ttp.Parser()

	# call twitter
	url = 'https://api.twitter.com/1.1/search/tweets.json'
	payload = {
		'q': search_items, 
		'lang': 'en',
		'result_type': 'mixed',
		'count': '100'
		#'until': Get_Time()['today']
	}
	
	r = requests.get(url=url, auth=_auth, params=payload)
	result = r.json()

	# Format the tweet
	for row in result['statuses']:
		tw_result = p.parse(row['text'])
		row['text_html'] = tw_result.html
		
		# Format the creation date
		tweet_date = format_date(row['created_at'])
		row['date_text'] = tweet_date
	
	return result

	
def main():
	
	result = req_twitter()
	pprint (result)
	
	return 0

if __name__ == '__main__':
	main()
