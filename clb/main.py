#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
from clb.scraper.game_scraper import GScraper
from clb.scraper.box_scraper import BScraper
from clb.scraper.play_scraper import PScraper
from clb.scraper.roster_scraper import RScraper

__author__ = 'prs_watch'

def main():
	"""
	CLB main method
	"""

	# init parser
	parser = argparse.ArgumentParser(description="commandline baseball")

	# set variable
	parser.add_argument('-b','--box',type=str,default='no_box')
	parser.add_argument('-d','--day',type=str,default=datetime.now().strftime("%Y%m%d"))
	parser.add_argument('-p','--play',type=str,default='no_play')
	parser.add_argument('-r','--roster',type=str,default='no_roster')
	parser.add_argument('-s','--score',action='store_true')
	parser.add_argument('--grep',type=str,default='no_grep')

	# return object
	args = parser.parse_args()

	# execute process
	process(args)

def process(args):
	"""
	execute scraping
	:param args: given params
	"""
	if args.box != 'no_box':
		BScraper(args.day,args.box,args.play,args.score,args.roster,args.grep).scrape()
	elif args.play != 'no_play':
		PScraper(args.day,args.box,args.play,args.score,args.roster,args.grep).scrape()
	elif args.roster != 'no_roster':
		RScraper(args.day,args.box,args.play,args.score,args.roster,args.grep).scrape()
	else:
		GScraper(args.day,args.box,args.play,args.score,args.roster,args.grep).scrape()

if __name__ == '__main__':
	main()