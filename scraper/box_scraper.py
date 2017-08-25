#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import texttable as ttb
from scraper.scraper import Scraper
from utils import Utils

__author__ = 'prs-watch'

class BScraper(Scraper):
	def scrape(self):
		self._scrape_scoreboard()

	def _scrape_scoreboard(self):
		"""
		scrape scoreboard
		"""
		games = self._get_games()
		selected_game = games[int(self.box)]

		boxscore_path = Utils.find_attr(selected_game,'game_data_directory')
		boxscore_url = 'http://gd2.mlb.com' + boxscore_path + '/' + 'boxscore.xml'

		html = Utils.get_content(boxscore_url,self.PARSER)

		if html == 'clb end':
			sys.exit()

		boxscore_all = Utils.find_tag(html,'boxscore')

		# basic info
		away_team_name = Utils.find_attr(boxscore_all,'away_fname')
		home_team_name = Utils.find_attr(boxscore_all,'home_fname')

		#score board info
		score_all = Utils.find_tag(boxscore_all,'linescore')
		away_total_runs = Utils.find_attr(score_all,'away_team_runs')
		home_total_runs = Utils.find_attr(score_all,'home_team_runs')
		away_total_hits = Utils.find_attr(score_all,'away_team_hits')
		home_total_hits = Utils.find_attr(score_all,'home_team_hits')
		away_total_errs = Utils.find_attr(score_all,'away_team_errors')
		home_total_errs = Utils.find_attr(score_all,'home_team_errors')

		innings = Utils.find_all_tags(score_all,'inning_line_score')

		table_contents = []
		header = []
		away = []
		home = []
		align = []
		header.append('TEAM')
		away.append(away_team_name)
		home.append(home_team_name)

		for inning in innings:
			align.append('c')
			header.append(Utils.find_attr(inning,'inning'))
			away.append(Utils.find_attr(inning,'away'))
			home.append(Utils.find_attr(inning,'home'))

		header.extend(['R','H','E'])
		away.extend([away_total_runs,away_total_hits,away_total_errs])
		home.extend([home_total_runs,home_total_hits,home_total_errs])
		align.extend(['c','c','c','c'])

		table_contents.append(header)
		table_contents.append(away)
		table_contents.append(home)

		table = ttb.Texttable()
		table.set_cols_align(align)
		table.add_rows(table_contents)

		print (table.draw())