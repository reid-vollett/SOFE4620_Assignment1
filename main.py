# Author: Reid Vollett
# Data Mining Assignment 1

import http.client
import json
import csv
import requests

# Switch flag for printing player stats
print_player_stats = 0

# Program takes a while to collect all the info from the APIs
print("\nRunning data collection, this may take a few minutes...")

# Generate CSV file handler for writing
team_csvdata = open('team_data.csv', 'w')
player_csvdata = open('player_data.csv', 'w')

# Generate CSV writer object
team_csvwriter = csv.writer(team_csvdata)
player_csvwriter = csv.writer(player_csvdata)

# Get readable JSON response from NHL API for NHL Teams
response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
nhl_data = response.json()

nhl_teams = nhl_data['teams']

# Determine if header for CSV file has been written
headerSig = 0
# Iterate through dict and write to CSV file
for team in nhl_teams:
        if headerSig == 0:
            # Write header to CSV file
            team_csvwriter.writerow(team.keys())
            headerSig = 1
        team_csvwriter.writerow(team.values())
    
nhlteam_list = []
for team in nhl_teams:
    nhlteam_list.append(team['id'])

player_list = []
playerlink_list = []

for team in nhlteam_list:
    # Get readable JSON response from NHL API for Team Rosters
    rLink = ("https://statsapi.web.nhl.com/api/v1/teams/%s?expand=team.roster" % team)
    response = requests.get(rLink)
    team_data = response.json()

    player_roster = team_data['teams'][0]['roster']['roster']
    
    for player in player_roster:
        player_list.append(player['person']['id'])
        playerlink_list.append(player['person']['link'])

# Determine if header for CSV file has been written
headerSig = 0
# Iterate through dict and write to CSV file
for player_id in player_list:
    # Get readable JSON response from NHL API for Player Stats
    rLink = ("https://statsapi.web.nhl.com/api/v1/people/%s?expand=person.stats&stats=yearByYear" % player_id)
    response = requests.get(rLink)
    data = response.json()
    player_data = data['people']
    for player in player_data:
        player_basic = data['people'][0]
        stats_data = data['people'][0]['stats'][0]['splits']
        
        #Important Note!
        # Some data is kept as a dictionary for a few key reasons, first of
        # which the API is not always consistent as some players may be missing
        # statistics or have unique statis for one season (ie. https://goo.gl/nUj9Ja).
        # The second reason to keep some data in the dictionary format is that it
        # allows easier manipulation if/when this data is used for data processing
        # in general use cases or in machine learning. Program readability was preffered
        # over human readability.
            
        if print_player_stats:
            player_name = player_basic['fullName']
            player_team = player_basic['currentTeam']['name']
            player_type = player_basic['primaryPosition']['name']
           
            print("\n"+player_name)
            print(player_team)
            print(player_type)
            print("-------------")
            
            for stat in stats_data:
                season_date = stat['season']
                print("Season: %s" % season_date)
                print(stat['stat'].keys())
                print(stat['stat'].values())
            
                '''
                player_assists = stat['stat']['assists']
                player_goals = stat['stat']['goals']
                player_pim = stat['stat']['pim']
                player_games = stat['stat']['games']
                player_penalty = stat['stat']['penaltyMinutes']
                player_points = stat['stat']['points']
            
                print("Assists: %s" % player_assists)
                print("Goals: %s" % player_goals)
                print("PIM: %s" % player_pim)
                print("Games: %s" % player_games)
                print("Penalty Time: %s" % player_penalty)
                print("Points: %s" % player_points)
                '''
                
        if headerSig == 0:
            # Write header to CSV file
            player_csvwriter.writerow(player.keys())
            headerSig = 1
        player_csvwriter.writerow(player.values())

print("\nFinished running!\n\n")
#team_csvwriter.close()
#player_csvwriter.close()