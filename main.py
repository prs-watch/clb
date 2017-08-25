#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
from scraper.game_scraper import GScraper
from scraper.box_scraper import BScraper

__author__ = 'prs_watch'

def main():
	"""
	CLB main method
	"""

	# init parser
	parser = argparse.ArgumentParser(description="pitchfx commandline tool")

	# set variable
	parser.add_argument('-d','--day',type=str,default=datetime.now().strftime("%Y%m%d"))
	parser.add_argument('-b','--box',type=str,default='no_box')

	# return object
	args = parser.parse_args()

	# execute process
	process(args)

def process(args):
	"""
	execute scraping
	:param args: params from commandline
	"""
	if args.box != 'no_box':
		BScraper(args.day,args.box).scrape()
	else:
		GScraper(args.day,args.box).scrape()

if __name__ == '__main__':
	main()