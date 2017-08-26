#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import texttable as ttb
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
			print('error: 404 not found.')
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
			return 'none'

	@classmethod
	def draw_table(self,contents,aligns,is_deco):
		"""
		draw table
		:param contents: table contents
		:param aligns: aligns
		:param is_deco: deco flag 
		"""
		table = ttb.Texttable()
		
		if is_deco:
			table.set_deco(ttb.Texttable.HEADER)
		table.set_cols_align(aligns)
		table.add_rows(contents)
		print(table.draw())