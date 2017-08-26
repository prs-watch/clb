#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup

__author__ = 'prs-watch'

class Utils(object):

	@classmethod
	def get_content(self,url,parser):
		"""
		get http content
		:param url: url
		:param parser:parser
		"""
		res = requests.get(url)

		if res.status_code == requests.codes.ok:
			return BeautifulSoup(res.text,parser)
		else:
			print('Sorry! No Such Page...')
			sys.exit()

	@classmethod
	def find_tag(self,content,tag):
		"""
		find first tag
		:param content: http content
		:param tag: tag
		"""
		return content.find(tag)

	@classmethod
	def find_all_tags(self,content,tag):
		"""
		find all tags
		:param content: http content
		:param tag: tag
		"""
		return content.find_all(tag)
		
	@classmethod
	def find_attr(self,content,attr):
		"""
		find attributes
		:param content: http content
		:param attr: attribute
		"""
		if content.get(attr):
			return content.get(attr)
		else:
			return 'None'