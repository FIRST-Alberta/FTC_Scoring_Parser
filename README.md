# FTC_Scoring_Parser

This application will parse JSON information provided by the FTC 
Scoring system and provide either the Event Rankings, League Rankings 
or both. 
A Location to fetch the data from must be provided and 3 options are 
available:
1. Filename: A full or relative path to the JSON file manually downloaded from the scoring system.
2. URL: A full URL to the JSON file.
3. URL Information: Partial URL information used to construct a full URL. Hostname/IP Address and Event Code are required.

## Application Usage

usage: ranking_parser.py [-h] [--file PATH] [--url URL] [--event] [--league] [--host IP-ADDR] [--eventcode EVENT]

options:
  * -h, --help            show this help message and exit
  * --file PATH, -f PATH  Filepath to a JSON with results to parse.
  * --url URL, -u URL     Network Location to fetch JSON results.
  * --event, -e           If true, event rankings will be displayed
  * --league, -l          If true, league results will be displayed
  * --host IP-ADDR, -H IP-ADDR Hostname or IP address for the scoring system. Must also provide event code.
  * --eventcode EVENT, -c EVENT FIRST Event Code, must be provide with a host.

## Application Prerequisites

This application will run on Windows and Linux but it will need a few packages.

- Python >= 3.6
- The Pandas Python module
