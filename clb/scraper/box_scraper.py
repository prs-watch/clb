#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import texttable as ttb
from clb.scraper.scraper import Scraper
from clb.utils import Utils

__author__ = 'prs-watch'

# scraper class for boxscore
class BScraper(Scraper):
	def scrape(self):
		games = self._get_games()
		selected_game = games[int(self.box)]

		boxscore_path = Utils.find_attr(selected_game,'game_data_directory')
		boxscore_url = 'http://gd2.mlb.com' + boxscore_path + '/' + 'boxscore.xml'

		html = Utils.get_content(boxscore_url,self.PARSER)

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
		aligns = []
		header.append('TEAM')
		away.append(away_team_name)
		home.append(home_team_name)

		for inning in innings:
			aligns.append('c')
			header.append(Utils.find_attr(inning,'inning'))
			away.append(Utils.find_attr(inning,'away'))
			home.append(Utils.find_attr(inning,'home'))

		header.extend(['R','H','E'])
		away.extend([away_total_runs,away_total_hits,away_total_errs])
		home.extend([home_total_runs,home_total_hits,home_total_errs])
		aligns.extend(['c','c','c','c'])

		table_contents.append(header)
		table_contents.append(away)
		table_contents.append(home)

		Utils.draw_table(table_contents,aligns,True)

	def _scrape_boxscore(self,boxscore,away_team_name,home_team_name):
		"""
		scrape boxscore
		:param boxscore: boxscore contents
		:param away_team_name: away team name
		:param home_team_name: home team name
		"""
		batting_aligns = ['c','c','c','c','c','c','c','c','c','c','c']
		pitching_aligns = ['c','c','c','c','c','c','c','c','c']

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
				
				if bo_id != 'none':
					pass
				else:
					bo_id = '---'

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

		print('\t'.join(['***',away_team_name,'***']))
		Utils.draw_table(away_batting,batting_aligns,False)
		Utils.draw_table(away_pitching,pitching_aligns,False)
		print('')
		print('\t'.join(['***',home_team_name,'***']))
		Utils.draw_table(home_batting,batting_aligns,False)
		Utils.draw_table(home_pitching,pitching_aligns,False)