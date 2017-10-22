#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
from clb.factory.scraper_factory import ScraperFactory

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
	scraper = ScraperFactory(args).create_scraper()
	scraper.scrape()

if __name__ == '__main__':
	main()