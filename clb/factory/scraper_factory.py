#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clb.scraper.game_scraper import GScraper
from clb.scraper.box_scraper import BScraper
from clb.scraper.play_scraper import PScraper
from clb.scraper.roster_scraper import RScraper

__author__ = 'prs_watch'

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
			# boxscore scraper.
			return BScraper(self.args.day,self.args.box,self.args.play,self.args.score,self.args.roster,self.args.grep)
		elif self.args.play != 'no_play':
			# play-by-play scraper.
			return PScraper(self.args.day,self.args.box,self.args.play,self.args.score,self.args.roster,self.args.grep)
		elif self.args.roster != 'no_roster':
			# roster scraper.
			return RScraper(self.args.day,self.args.box,self.args.play,self.args.score,self.args.roster,self.args.grep)
		else:
			# game list scraper.
			return GScraper(self.args.day,self.args.box,self.args.play,self.args.score,self.args.roster,self.args.grep)