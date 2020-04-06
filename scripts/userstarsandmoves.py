#import risk
import college_football_risk as risk
import pandas as pd

#set API's from Risk
players_api = risk.PlayersApi()
stats_api = risk.StatsApi()
#retreives players that have opted out and puts them in a list together
#need to make sure that this points towards the opt out list 
optOut = pd.read_csv('CFB/optout.csv')

#sets up dataframe for collection
df = pd.DataFrame()

#sets up lists to add to dataframe
playerList = []
starList = []
movelist = []
daylist = []
#takes team, returns list of members, minus players that haven't played in season 2
#checks that they haven't opted out as well
def teamMembers(team_Check,day):
    # Get a list of players by team
    players = players_api.get_players(team=team_Check)
    for player in players:
        #opt out collected from Github file, saved as csv, and then put into a list called optOut in this file
        if(player.last_turn.season ==2 and player.player not in optOut):
            daylist.append(day)
            playerList.append(player.player)
            starList.append(player.last_turn.stars)
            movelist.append(players_api.get_player(player.player).turns[0].territory)

#uses teamMembers to populate players column of df
#gets active day from stats API
def getTurnsAmount():
    turns = stats_api.get_turns()
    for day in turns:
        if(day.active ==True):
            return day.day

day = getTurnsAmount()           
teamMembers("Michigan",day)

df["day"] = daylist
df["players"] = playerList
df["stars"] = starList
df["move"] = movelist

#sends data to csv, can be changed to append
#df.to_csv(r'CFB/OSUMoves.csv', index = False, header=True)
df.to_csv(r'CFB/michmoves.csv', index = False, header=True)
print("Fin")

