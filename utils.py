#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

class Utils(object):
	@classmethod
	def get_content(self,url,parser):
		"""
		get http content
		:param url: url
		:param parser:parser
		"""
		res	=	requests.get(url)

		if res.status_code == requests.codes.ok:
			return BeautifulSoup(res.text,parser)
		else:
			res.raise_for_status()
