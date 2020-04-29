import pandas as pd
import matplotlib.pyplot as plt

#gets roll log
def get_rolls(current_day):
    url = 'https://collegefootballrisk.com/api/roll/log?season=2&day='+str(current_day)
    df = pd.read_json(url)
    gf = []
    for territory in df['territoryRolls']:
        gf.append(territory)
    gf = pd.DataFrame(gf)
    return gf

# gets 'heat' data
def heat(current_day): 
    url = 'https://collegefootballrisk.com/api/heat?season=2&day='+str(current_day)
    temp = pd.read_json(url)
    return temp

day = 37
rolls = get_rolls(day)
heat = heat(day-1)
rolls['day']=day
heat['day'] = day
rolls.to_csv('data/rolls.csv',index = False,mode='a', header=False)
heat.to_csv('data/territory_info.csv',index = False,mode='a', header=False)
#df = pd.merge(rolls,heat,on=['winner','territory'])
#df['randint']=df['randomNumber']/df['power']
#print(df.head())
#print(df.groupby('winner')['randint','players','power','randomNumber'].mean())
print('fin')