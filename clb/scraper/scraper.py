#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clb.utils import Utils

__author__ = 'prs-watch'

# base scraper class
class Scraper(object):
	DELIMITER = '/'
	BASE_URL = 'http://gd2.mlb.com/components/game/mlb'
	YMD_FORMAT = 'year_{year}/month_{month}/day_{day}'
	PARSER = 'lxml'

	def __init__(self,timestamp,box,play,score,roster,grep):
		"""
		init
		:param timestamp: day
		:param box: boxscore flag
		:param score: score play flag
		:param roster: roster flag
		:param grep: grep word
		"""
		self.params = {
			'year'	:	timestamp[0:4]
		,	'month'	:	timestamp[4:6]
		,	'day'	:	timestamp[6:8]
		}

		self.box = box
		self.play = play
		self.score = score
		self.roster = roster
		self.grep = grep

	def _get_games(self):
		"""
		get all games from base url
		"""
		base_url = self.DELIMITER.join([
				self.BASE_URL
			,	self.YMD_FORMAT.format(**self.params)
			,	'epg.xml'
			])
		html = Utils.get_content(base_url,self.PARSER)
		return Utils.find_all_tags(html,'game')