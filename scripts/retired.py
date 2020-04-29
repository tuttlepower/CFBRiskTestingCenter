
import pandas as pd 

# Will get the rolls that have been provided, so 30 - current day
def get_rolls(current_day):
    df = []
    for x in range(30, current_day): 
        url = 'https://collegefootballrisk.com/api/roll/log?season=2&day='+str(current_day)
        temp = pd.read_json(url)
        for territory in temp['territoryRolls']:
            territory['day']= x
            df.append(territory)
    df = pd.DataFrame(df)
    return df

# Will get the territory info (heat) for days that have roll data, so 30 - current day
def individual_territories(current_day):
    df =pd.DataFrame()
    for x in range(30, current_day): 
        url = 'https://collegefootballrisk.com/api/heat?season=2&day='+str(x)
        temp = pd.read_json(url)
        temp['day'] = x
        #print(temp.head())
        df = df.append(temp)
    return df

# Will compare the territory info to the roll data to find the randint dist.
def territory_ints(current_day):
    return True

rolls = get_rolls(37)
territory_info = individual_territories(37)
print("Rolls")
print(rolls.shape)
print(rolls.head())
#print(rolls.tail())
print("Territory")
print(territory_info.shape)
print(territory_info.head())

rolls.to_csv('data/rolls.csv',index=False)
territory_info.to_csv('data/territory_info.csv',index=False)