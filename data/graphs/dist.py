import plotly.express as px
import pandas as pd 

def getTeamData(team,day):
    temp = pd.read_json (r'https://collegefootballrisk.com/api/team/players?season=2&day='+str(day)+'&team='+str(team).replace(" ", "%20"))
    return temp

gf = getTeamData("Michigan",1)
d = gf['territory'].value_counts()
temp = pd.DataFrame(d)
fig = px.pie(gf, values='territory',names='territory')
fig.show()

print(d.head())
print(d.shape)