import pandas as pd 

def getTeamData(team,day):
    temp = pd.read_json (r'https://collegefootballrisk.com/api/team/players?season=2&day='+str(day)+'&team='+str(team).replace(" ", "%20"))
    return temp

def teamlist():
    print("test")

def daysummary(team,day):
    team = team
    day = day
    temp = getTeamData(team,day)
    print("Summary: Day",day,",",team)
    print("Players: ", len(temp['player']))
    print("Distribution:")
    print(temp['territory'].value_counts(normalize=True))

def totalsummary(team):
    print("test")

daysummary("Ohio State",25)