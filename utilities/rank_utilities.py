
def rank_sort(team_points: tuple):
    """This provides the primary, secondary, and tertiary sort keys to sort a
    dictionary by team RP, TBP1, and TBP2"""
    rp = team_points[1]["RP"]
    tbp1 = team_points[1]["TBP1"]
    tbp2 = team_points[1]["TBP2"]
    return (rp, tbp1, tbp2) 

def sort_Rank_Dict(rank_dict: dict) -> dict:
    """Sorts the provided dictionary by RP, TBP1, and TBP2.
       Python3 > 3.6 respects order of insertion for dictionaries"""
    sorted_rank_dict = {}
    for rank in sorted(rank_dict.items(), key=rank_sort, reverse=True):
        # rank[0] is the team number, rank[1] is a dict that contains RP, TBP1, and TBP2
        sorted_rank_dict[rank[0]] = rank[1]
    return sorted_rank_dict

def average_Team_Match_Results(eventData: dict) -> dict:
    """Takes a dict of teams with RP, TBP1, and TBP2 per match 
    and averages it based on the number of matches played by each team."""
    averaged_rank_dict = {}
    # Variables to be reset for each team
    numOfMatches = 0
    rankPoints = 0
    tieBreak1 = 0
    tieBreak2 = 0

    # Process 1 team at a time
    for team in eventData.keys():
        numOfMatches = len(eventData[team])

        #Average each point category
        for match in eventData[team].keys():
            rankPoints += eventData[team][match]["RP"]
            tieBreak1 += eventData[team][match]["TBP1"]
            tieBreak2 += eventData[team][match]["TBP2"]
        eventData[team]["RP"] = float(rankPoints)/numOfMatches
        eventData[team]["TBP1"] = float(tieBreak1)/numOfMatches
        eventData[team]["TBP2"] = float(tieBreak2)/numOfMatches

        #Reset variables
        numOfMatches = 0
        rankPoints = 0
        tieBreak1 = 0
        tieBreak2 = 0

        # Add Averages to rank dictionary
        if team not in averaged_rank_dict:
            averaged_rank_dict[team] = {}
        averaged_rank_dict[team]['RP'] = eventData[team]["RP"]
        averaged_rank_dict[team]['TBP1'] = eventData[team]["TBP1"]
        averaged_rank_dict[team]['TBP2'] = eventData[team]["TBP2"]
    
    return averaged_rank_dict

def Determine_Ranks(eventData: dict) -> dict:
    """This function determines ranks from a collection of match data sorted by team."""
    unsorted_rank_dict = average_Team_Match_Results(eventData)
    return sort_Rank_Dict(unsorted_rank_dict)