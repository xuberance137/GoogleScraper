#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pre-reqs:
# brew install chromedriver -> for running the chrome webdriver using selenium 

# Usage:
# python3 run_scraper.py "learning django" scraper_search_links.json

"""
Shows how to control GoogleScraper programmatically.
"""

import sys
from GoogleScraper import scrape_with_config, GoogleSearchError
from GoogleScraper.database import ScraperSearch, SERP, Link
import json

def run_crawler(searchString, jsonFileName):
    # See in the config.cfg file for possible values
    config = {
        'keyword': searchString,
        'search_engines':['google', 'bing'],
        'num_pages_for_keyword': 10,
        'output_filename': jsonFileName,
        'SCRAPING': {
            'use_own_ip': 'True',
            'num_pages_for_keyword': 1
        },
        'SELENIUM': {
            'sel_browser': 'chrome',
        },
        'GLOBAL': {
            'do_caching': 'False'
        }
    }

    try:
        sqlalchemy_session = scrape_with_config(config)
    except GoogleSearchError as e:
        print("GoogleSearchError")
        print(e)

def read_json(jsonFileName):

    data = json.load(open(jsonFileName))
    desc = []
    link = []

    for item1 in data:
        for item in item1['results']:
            link.append(item['link'])
            desc.append(item['title'])

    return link, desc


### MAIN FUNCTION ###
if __name__ == '__main__':

    usage = 'Usage: {} <search string> <json file name>'.format(sys.argv[0])
    if len(sys.argv) != 3:
        print(usage)
    else:
        queryString = sys.argv[1]
        jsonFileName = sys.argv[2]
        print("Basic text search using Selenium Crawler <><> ")
        run_crawler(queryString, jsonFileName)
        link, desc = read_json(jsonFileName)

        for index in range(len(link)):
            print(link[index], desc[index])




