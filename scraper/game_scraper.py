#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scraper.scraper import Scraper
from utils import Utils

__author__ = 'prs-watch'

class GScraper(Scraper):
	def scrape(self):
		"""
		scrape game info
		"""
		games = self._get_games()

		table_contents = []
		aligns = ['c','c','c','c','c']

		table_contents.append([
				'NO'
			,	'VENUE'
			,	'HOME_TEAM'
			,	'AWAY_TEAM'
			,	'RESULT'
			])

		no = 0

		for game in games:

			content = []

			venue = Utils.find_attr(game,'venue')
			away_team_name = Utils.find_attr(game,'away_team_name')
			home_team_name = Utils.find_attr(game,'home_team_name')
			away_win = Utils.find_attr(game,'away_win')
			away_loss = Utils.find_attr(game,'away_loss')
			home_win = Utils.find_attr(game,'home_win')
			home_loss = Utils.find_attr(game,'home_loss')
			away_team_runs = Utils.find_attr(game,'away_team_runs')
			home_team_runs = Utils.find_attr(game,'home_team_runs')

			if away_team_runs == 'none':
				away_team_runs = '*'

			if home_team_runs == 'none':
				home_team_runs = '*'

			away = away_team_name + '(' + away_win + '-' + away_loss + ')'
			home = home_team_name + '(' + home_win + '-' + home_loss + ')'
			result = away_team_runs + '-' + home_team_runs

			content.append(str(no))
			content.append(venue)
			content.append(away)
			content.append(home)
			content.append(result)

			table_contents.append(content)

			no += 1

		Utils.draw_table(table_contents,aligns,True)