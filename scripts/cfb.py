#https://github.com/BlueSCar/college-football-risk-python
#https://collegefootballrisk.com/api/docs/?url=/api-docs.json
#https://collegefootballrisk.com/
#https://discordapp.com/channels/587696149868314644/587696149868314652
#https://www.reddit.com/r/OSUcfbRisk/

#import risk
import college_football_risk as risk
import pandas as pd
#set API's
players_api = risk.PlayersApi()
team_api = risk.TeamsApi()
territories_api = risk.TerritoriesApi()
stats_api = risk.StatsApi()

df = pd.DataFrame

def starPower(player_name):
    #get star power for single player
    # This could easily be changed to find overall, total_turns,game_turns,mvps,streak,awards
    #takes player name that gets passed through when starPower is called
    player_name = player_name
    player = players_api.get_player(player_name)
    return player.ratings.overall
    
def teamMembers(team_Check):
    return True

#takes name, returns starpower
def starPower(player_name):
    player_name = player_name
    player = players_api.get_player(player_name)
    return player.ratings.overall

#takes name and day, returns move, if no move, returns None. Only for season 2 
def getMove(player_name,day):
    for turns in players_api.get_player(player_name).turns:
        if(turns.season ==2):
            if (turns.day == day):
                return turns.territory

#placeholder for getting orders that are sent
def getOrder(player_name,day):
    order = "test"
    return order

#placeholder for exporting data somewhere
def exportData(day,playerList):
    f = open("CFB/CFBData.csv", "x")
    for player in playerList:
        for turns in players_api.get_player.turns:
            f.write("{0}")

#gets active day from stats API
def getTurnsAmount():
    turns = stats_api.get_turns()
    for day in turns:
        if(day.active ==True):
            return day.day


day = getTurnsAmount()
playerList = []
starList = []

# Get a list of players by team
players = players_api.get_players(team="Ohio State")
for player in players:
    playerList.append(player.player)
    starList.append(starPower(player.player))
df["players"] = playerList
#df["stars"] = starList

print("Day: Done")
print(df.head())
print("Playerlist: Done")
#collateData(playerList,day)
#excelFile(playerList,day)
print("Excel File: Fin")