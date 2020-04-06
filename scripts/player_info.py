#import risk
import college_football_risk as risk
import pandas as pd
#set API's
players_api = risk.PlayersApi()
team_api = risk.TeamsApi()
territories_api = risk.TerritoriesApi()
stats_api = risk.StatsApi()

g = open("CFB/CFBData.csv", "w")

#takes team, returns list of members
def teamMembers(team_Check):
    
    playerList = []
    # Get a list of players by team
    players = players_api.get_players(team=team_Check)
    for player in players:
        playerList.append(player.player)
    return playerList

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

def collateData(playerList,day):
    df= pd.DataFrame(playerList)
    df.columns = ["player"]
    temp = []
    for player in playerList:
        temp.append(starPower(player))
    print(temp)


def excelFile(playerList,day):
    for player in playerList:
        g.write("{0},{1},".format(player,starPower(player)))
        for x in range(1,day+1):
            g.write("{0},{1},".format(getMove(player,x),getOrder(player,x)))
    g.write("\n")

#takes team, returns list of members
def teamMembersSpecificDate(team_Check,season):
    season = season
    playerList = []
    # Get a list of players by team
    players = players_api.get_players(team=team_Check)
    for player in players:
        playerList.append(player.player)
    return playerList

day = getTurnsAmount()
print("Day: Done")
playerList = teamMembers("Ohio State")
print("Playerlist: Done")
#collateData(playerList,day)
print(teamMembersSpecificDate("Ohio State",2))
#excelFile(playerList,day)
print("Excel File: Fin")