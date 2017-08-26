#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scraper.scraper import Scraper
from utils import Utils

# scraper class
class PScraper(Scraper):
	def scrape(self):
		games = self._get_games()
		selected_game = games[int(self.play)]
		game_info_path = Utils.find_attr(selected_game,'game_data_directory')
		play_by_play_url = 'http://gd2.mlb.com' + game_info_path + '/' + 'game_events.xml'
		
		table_contents = []
		header = ['INNING','BATTER_NO','DESCRIPTION','SCORE']
		aligns = ['c','c','l','c']
		table_contents.append(header)

		html = Utils.get_content(play_by_play_url,self.PARSER)
		all_innings = Utils.find_all_tags(html,'inning')

		for single_inning in all_innings:
			inning = []
			inning_no = Utils.find_attr(single_inning,'num')

			top = Utils.find_tag(single_inning,'top')
			bottom = Utils.find_tag(single_inning,'bottom')
			top_atbats = Utils.find_all_tags(top,'atbat')
			bottom_atbats = Utils.find_all_tags(bottom,'atbat')

			for top_atbat in top_atbats:
				result = []

				away_team_runs = Utils.find_attr(top_atbat,'away_team_runs')
				home_team_runs = Utils.find_attr(top_atbat,'home_team_runs')
				score = away_team_runs + '-' + home_team_runs

				result.append(inning_no)
				result.append(Utils.find_attr(top_atbat,'num'))
				result.append(Utils.find_attr(top_atbat,'des'))
				result.append(score)

				inning.append(result)

			for bottom_atbat in bottom_atbats:
				result = []
				
				away_team_runs = Utils.find_attr(bottom_atbat,'away_team_runs')
				home_team_runs = Utils.find_attr(bottom_atbat,'home_team_runs')
				score = away_team_runs + '-' + home_team_runs

				result.append(inning_no)
				result.append(Utils.find_attr(bottom_atbat,'num'))
				result.append(Utils.find_attr(bottom_atbat,'des'))
				result.append(score)

				inning.append(result)

			table_contents.extend(inning)

		if self.score:
			score_plays_table = []
			score_plays_table_aligns = ['c','l','c']

			score_plays_table.append([
					'INNING'
				,	'DESCRIPTION'
				,	'SCORE'
				])

			for table_content in table_contents:
				score_play = []

				if 'scores' in table_content[2] or 'homers' in table_content[2]:
					score_play.append(table_content[0])
					score_play.append(table_content[2])
					score_play.append(table_content[3])
					score_plays_table.append(score_play)

			Utils.draw_table(score_plays_table,score_plays_table_aligns,False)
		else:
			Utils.draw_table(table_contents,aligns,False)