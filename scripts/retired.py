#import risk
import college_football_risk as risk
import pandas as pd
#set API's from Risk
players_api = risk.PlayersApi()
team_api = risk.TeamsApi()
territories_api = risk.TerritoriesApi()
stats_api = risk.StatsApi()

#retreives players that have opted out and puts them in a list together
optOut = pd.read_csv('CFB/optout.csv')
#sets up dataframe for collection
df = pd.DataFrame()
#sets up lists
playerList = []
starList = []

#gets active day from stats API
def getTurnsAmount():
    turns = stats_api.get_turns()
    for day in turns:
        if(day.active ==True):
            return day.day

#takes team, returns list of members, minus players that haven't played in season 2
#checks that they haven't opted out as well
def teamMembers(team_Check):
    # Get a list of players by team
    players = players_api.get_players(team=team_Check)
    for player in players:
        #opt out collected from Github file, saved as csv, and then put into a list called optOut in this file
        if(player.last_turn.season ==2 and player.player not in optOut):
            playerList.append(player.player)
            starList.append(player.last_turn.stars)


#takes name and day, returns move, if no move, returns None. Only for season 2,
#doesn't work well on large lists 
def getMove(player_name,day):
    for turns in players_api.get_player(player_name).turns:
        if(turns.season ==2):
            if (turns.day == day):
                return turns.territory
    
#sets days
day = getTurnsAmount()

#uses teamMembers to populate players column of df
teamMembers("Ohio State")
df["players"] = playerList
df["stars"] = starList

print(df.describe())

