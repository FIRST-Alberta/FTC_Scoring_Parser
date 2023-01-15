
import argparse
import pandas
from IPython.display import display
from utilities.json_utilities import *
from utilities.match_processor import Create_Event_Data
from utilities.rank_utilities import Determine_Ranks


#===================================================================
#================= Ranking Parser Entry Point ======================
#===================================================================
"""This application will parse JSON information provided by the FTC 
Scoring system and provide either the Event Rankings, League Rankings 
or both. 
A Location to fetch the data from must be provided and 3 options are 
available:
    1. Filename: A full or relative path to the JSON file manually 
                 downloaded from the scoring system.
    2. URL: A full URL to the JSON file.
    3. URL Information: Partial URL information used to construct a full URL.
                        Hostname/IP Address and Event Code are required."""
# Setup the argument parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--file", "-f", type=str, metavar="PATH", help="Filepath to a JSON with results to parse.")
arg_parser.add_argument("--url", "-u", type=str, metavar="URL", help="Network Location to fetch JSON results.")
arg_parser.add_argument("--event", "-e", action="store_true", help="If true, event rankings will be displayed")
arg_parser.add_argument("--league", "-l", action="store_true", help="If true, league results will be displayed")
arg_parser.add_argument("--host","-H", type=str, metavar="IP-ADDR", help="Hostname or IP address for the scoring system. Must also provide event code.")
arg_parser.add_argument("--eventcode", "-c", type=str, metavar="EVENT", help="FIRST Event Code, must be provide with a host.")
args = arg_parser.parse_args()

# Load the JSON from the specified location
if args.file:
    scores = load_JSON_From_File(args.file)
elif args.url:
    scores = load_JSON_From_URL(args.url)
elif args.host and args.eventcode:
    scores = load_JSON_From_URL("http://"+args.host+"/api/v2/events/"+args.eventcode+"/full/")
else:
    print("No data location provided!")
    print(arg_parser.print_help())
    exit(1)
if not scores:
    print("JSON data was not imported correctly!")
    print(arg_parser.print_help())
    exit(1)

# This is a global setting for the Tables that are outputed.
pandas.set_option('display.max_rows', None)

# Now check for which Tables should be outputted 

# This will print the Event Rankings
if args.event:
    matches = scores["matchList"]["matches"]
    eventResults = Determine_Ranks(Create_Event_Data(matches))
    print("The Winning Team is {}!".format(list(eventResults.keys())[0]))
    eventRanksTable = pandas.DataFrame({"Team Number": eventResults.keys(), 
                      "Ranking Points": (value["RP"] for value in eventResults.values()),
                      "Tie Breaker Points 1": (value["TBP1"] for value in eventResults.values()),
                      "Tie Breaker Points 2": (value["TBP2"] for value in eventResults.values())})
       
    display(eventRanksTable)

# This will print the league Rankings
if args.league:
    team_list = scores["combinedRankingsList"]["rankingList"]
    league_ranks = {}
    for team in team_list:
        league_ranks[team["ranking"]] = {"Team Number": team["team"], "Team Name": team["teamName"]}
    leagueTable = pandas.DataFrame(league_ranks)
    leagueTable = leagueTable.transpose()
    display(leagueTable)
