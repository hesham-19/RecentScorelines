import requests
import json
from private import rapidAPI_key
from team_ids import team_ids
# Enter the name of a team in the La Liga, EPL, or Serie A
# And it will return the most recent scorlines for that team


team = input("Enter team name ").lower()

url = f"https://api-football-v1.p.rapidapi.com/v2/fixtures/team/{team_ids[team]}/last/20"
headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': rapidAPI_key
}

response = requests.request("GET", url, headers=headers)


def printRecentScorelines():

    data = json.loads(response.text)

    for fixture in data['api']['fixtures']:
        if fixture['score']['fulltime'] is not None:
            homeTeam = fixture['homeTeam']['team_name']
            awayTeam = fixture['awayTeam']['team_name']

            if fixture['score']['extratime'] is None:
                final_score = fixture['score']['fulltime']
            else:
                final_score = fixture['score']['extratime']
            print(homeTeam, final_score, awayTeam, end=" ")

            if fixture['score']['penalty'] is not None:
                penalty_score = fixture['score']['penalty']
                print('(', penalty_score, ')', end='')

            print('')


printRecentScorelines()
