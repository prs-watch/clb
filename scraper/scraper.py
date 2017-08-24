#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

class Scraper(object):
	DELIMITER		=	'/'
	BASE_URL		=	'http://gd2.mlb.com/components/game/mlb'
	YMD_FORMAT		=	'year_{year}/month_{month}/day_{day}'
	PATTERN			=	r'([a-zA-Z]{3})mlb_([a-zA-Z]{3})mlb'
	PARSER			=	'lxml'

	def __init__(self, timestamp):
		"""
		init
		:param timestamp: day
		"""
		self.params 	=	{
				'year'	:	timestamp[0:4],
				'month'	:	timestamp[4:6],
				'day'	:	timestamp[6:8]
		}
		self.pattern	=	re.compile(self.PATTERN)