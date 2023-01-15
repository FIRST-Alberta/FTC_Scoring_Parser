

def processMatch(match: dict) -> dict:
    """This utility function takes a match dictionary from the JSON file
       and parses out the information we want, 
       including assigning RP, TBP1 and TBP2 for each match.
       
       This could be used to fetch individual match results in the future.
    """
    stats = {"red": {}, "blue": {}}
    if not match["matchBrief"]["finished"]:
        print("Match {} not finished! Not Processing".format(match["matchBrief"]["matchName"]))
        return {}
    else:
        print("Processing Match {}".format(match["matchBrief"]["matchName"]))

        stats["matchName"] = match["matchBrief"]["matchName"]
        stats["red"]["teams"] = [match["matchBrief"]["red"]["team1"], match["matchBrief"]["red"]["team2"]]
        stats["blue"]["teams"] = [match["matchBrief"]["blue"]["team1"], match["matchBrief"]["blue"]["team2"]]
        stats["red"]["points"] = {}
        stats["blue"]["points"] = {}

        if match["redScore"] > match["blueScore"]:
            stats["red"]["points"]["RP"] = 2
            stats["blue"]["points"]["RP"] = 0
        elif match["redScore"] < match["blueScore"]:
            stats["red"]["points"]["RP"] = 0
            stats["blue"]["points"]["RP"] = 2
        else:
            stats["red"]["points"]["RP"] = 1
            stats["blue"]["points"]["RP"] = 1
        
        stats["red"]["points"]["TBP1"] = match["red"]["auto"]
        stats["red"]["points"]["TBP2"] = match["red"]["end"]

        stats["blue"]["points"]["TBP1"] = match["blue"]["auto"]
        stats["blue"]["points"]["TBP2"] = match["blue"]["end"]

        stats["red"]["score"] = match["red"]
        stats["red"]["score"]["total"] = match["redScore"]

        stats["blue"]["score"] = match["blue"]
        stats["blue"]["score"]["total"] = match["blueScore"]
    
        return stats

def Create_Event_Data(matches: dict) -> dict:
    """Process a list of matches into Event Data.
    
    This will assign the match scores and ranking points to the participating teams
    in their respective alliances.
    """
    eventData = {}
    for match in matches:
        match_result = processMatch(match)

        # Skip adding results if it's empty, this occurs if the match isn't finished.
        if not match_result:
            continue
        for alliance in ["red", "blue"]:
            for team in match_result[alliance]["teams"]:
                if team not in eventData:
                    eventData[team] = {}
                eventData[team][match_result["matchName"]] = match_result[alliance]["points"]
    return eventData