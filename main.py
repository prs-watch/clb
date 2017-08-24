#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
from scraper.game_scraper import GameScraper

__author__ = 'prs_watch'

def main():
	"""
	main method
	"""

	# init parser
	parser = argparse.ArgumentParser(description="pitchfx commandline tool")

	# set variable
	parser.add_argument('-d','--day',type=str,default=datetime.now().strftime("%Y%m%d"))

	# return object
	args = parser.parse_args()

	process(args)


def process(args):
	GameScraper(args.day).scrape()

if __name__ == '__main__':
	main()