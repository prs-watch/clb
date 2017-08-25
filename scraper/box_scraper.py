#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import texttable as ttb
from scraper.scraper import Scraper
from utils import Utils

__author__ = 'prs-watch'

class BScraper(Scraper):
	def scrape(self):
		games = self._get_games()
		selected_game = games[int(self.box)]

		boxscore_path = Utils.find_attr(selected_game,'game_data_directory')
		boxscore_url = 'http://gd2.mlb.com' + boxscore_path + '/' + 'boxscore.xml'

		html = Utils.get_content(boxscore_url,self.PARSER)

		if html == 'end':
			sys.exit()

		boxscore = Utils.find_tag(html,'boxscore')

		# basic info
		away_team_name = Utils.find_attr(boxscore,'away_fname')
		home_team_name = Utils.find_attr(boxscore,'home_fname')

		self._scrape_scoreboard(boxscore,away_team_name,home_team_name)
		self._scrape_boxscore(boxscore,away_team_name,home_team_name)

	def _scrape_scoreboard(self,boxscore,away_team_name,home_team_name):
		"""
		scrape scoreboard
		:param boxscore: boxscore contents
		:param away_team_name: away team name
		:param home_team_name: home team name
		"""
		score_all = Utils.find_tag(boxscore,'linescore')
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

	def _scrape_boxscore(self,boxscore,away_team_name,home_team_name):
		"""
		scrape boxscore
		:param boxscore: boxscore contents
		:param away_team_name: away team name
		:param home_team_name: home team name
		"""
		batting_align = ['c','c','c','c','c','c','c','c','c','c','c']
		pitching_align = ['c','c','c','c','c','c','c','c','c']

		batting_header = ['BATTING','NAME','POS','AB','R','H','RBI','BB','SO','LOB','AVG']
		pitching_header = ['PITCHING','IP','H','R','ER','BB','SO','HR','ERA']

		away_batting = []
		home_batting = []
		away_pitching = []
		home_pitching = []

		away_batting.append(batting_header)
		home_batting.append(batting_header)
		away_pitching.append(pitching_header)
		home_pitching.append(pitching_header)

		teams_batting = Utils.find_all_tags(boxscore,'batting')
		teams_pitching = Utils.find_all_tags(boxscore,'pitching')

		bat_count = 0
		for team_batting in teams_batting:
			batters = Utils.find_all_tags(team_batting,'batter')
			for batter in batters:
				player = []
				bo_id = Utils.find_attr(batter,'bo')
				bo = bo_id[0:1] + '-' + bo_id[1:3]

				player.append(bo)
				player.append(Utils.find_attr(batter,'name'))
				player.append(Utils.find_attr(batter,'pos'))
				player.append(Utils.find_attr(batter,'ab'))
				player.append(Utils.find_attr(batter,'r'))
				player.append(Utils.find_attr(batter,'h'))
				player.append(Utils.find_attr(batter,'rbi'))
				player.append(Utils.find_attr(batter,'bb'))
				player.append(Utils.find_attr(batter,'so'))
				player.append(Utils.find_attr(batter,'lob'))
				player.append(Utils.find_attr(batter,'avg'))

				if bat_count == 0:
					home_batting.append(player)
				else:
					away_batting.append(player)

			bat_count += 1

		pit_count = 0
		for team_pitching in teams_pitching:
			pitchers = Utils.find_all_tags(team_pitching,'pitcher')
			for pitcher in pitchers:
				player = []

				out = Utils.find_attr(pitcher,'out')
				ip = str(int(out) // 3) + '.' + str(int(out) % 3)

				player.append(Utils.find_attr(pitcher,'name'))
				player.append(ip)
				player.append(Utils.find_attr(pitcher,'h'))
				player.append(Utils.find_attr(pitcher,'r'))
				player.append(Utils.find_attr(pitcher,'er'))
				player.append(Utils.find_attr(pitcher,'bb'))
				player.append(Utils.find_attr(pitcher,'so'))
				player.append(Utils.find_attr(pitcher,'hr'))
				player.append(Utils.find_attr(pitcher,'era'))

				if pit_count == 0:
					away_pitching.append(player)
				else:
					home_pitching.append(player)

			pit_count += 1

		away_batting_table = ttb.Texttable()
		away_batting_table.set_cols_align(batting_align)
		away_batting_table.add_rows(away_batting)

		home_batting_table = ttb.Texttable()
		home_batting_table.set_cols_align(batting_align)
		home_batting_table.add_rows(home_batting)

		away_pitching_table = ttb.Texttable()
		away_pitching_table.set_cols_align(pitching_align)
		away_pitching_table.add_rows(away_pitching)

		home_pitching_table = ttb.Texttable()
		home_pitching_table.set_cols_align(pitching_align)
		home_pitching_table.add_rows(home_pitching)

		print('\t'.join(['***',away_team_name,'***']))
		print(away_batting_table.draw())
		print(away_pitching_table.draw())
		print('')
		print('\t'.join(['***',home_team_name,'***']))
		print(home_batting_table.draw())
		print(home_pitching_table.draw())