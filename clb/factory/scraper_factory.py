#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clb.scraper.game_scraper import GScraper
from clb.scraper.box_scraper import BScraper
from clb.scraper.play_scraper import PScraper
from clb.scraper.roster_scraper import RScraper

__autho__ = 'prs_watch'

class ScraperFactory(object):

	def __init__(self,args):
		"""
		:params args: args
		"""
		self.args = args

	def create_scraper(self):
		"""
		create scraper.

		:return scraper: scraper class.
		"""
		if self.args.box != 'no_box':
			# print boxscore.
			return BScraper(self.args.day,self.args.box,self.args.play,self.args.score,self.args.roster,self.args.grep)
		elif self.args.play != 'no_play':
			# print play-by-play.
			return PScraper(self.args.day,self.args.box,self.args.play,self.args.score,self.args.roster,self.args.grep)
		elif self.args.roster != 'no_roster':
			# print roster.
			return RScraper(self.args.day,self.args.box,self.args.play,self.args.score,self.args.roster,self.args.grep)
		else:
			# print game list.
			return GScraper(self.args.day,self.args.box,self.args.play,self.args.score,self.args.roster,self.args.grep)