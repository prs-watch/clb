#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clb.scraper.scraper import Scraper
from clb.utils import Utils

__author__ = "prs-watch"

class RScraper(Scraper):
	def scrape(self):
		games = self._get_games()
		selected_game = games[int(self.roster)]
		game_info_path = Utils.find_attr(selected_game,'game_data_directory')
		roster_url = 'http://gd2.mlb.com' + game_info_path + '/' + 'players.xml'

		away_roster = []
		home_roster = []
		header = ['TEAM','NAME','POS']
		aligns = ['c','c','c']

		away_roster.append(header)
		home_roster.append(header)

		html = Utils.get_content(roster_url,self.PARSER)
		teams = Utils.find_all_tags(html,'team')

		for team in teams:
			roster = []
			type = Utils.find_attr(team,'type')
			team_nm = Utils.find_attr(team,'name')
			members = Utils.find_all_tags(team,'player')

			for member in members:
				members_info = []
				first_name = Utils.find_attr(member,'first')
				last_name = Utils.find_attr(member,'last')
				full_name = ' '.join([first_name,last_name])

				members_info.append(team_nm)
				members_info.append(full_name)
				members_info.append(Utils.find_attr(member,'position'))

				roster.append(members_info)

			if type == 'away':
				away_roster.extend(roster)
			else:
				home_roster.extend(roster)

		print('\t'.join(['***','away','***']))
		Utils.draw_table(away_roster,aligns,False)
		print('')
		print('\t'.join(['***','home','***']))
		Utils.draw_table(home_roster,aligns,False)
