# import pandas as pd
import pandas as pd
#currently at 14 as of 4/6/2020
#adds additional day 14 will be next
day = 20
temp = pd.read_json (r'https://collegefootballrisk.com/api/team/players?season=2&day='+str(day)+'&team=ohio%20state')
#creates df, and appends new data to it
#df = df.append(temp, ignore_index = True)
#outputs new data to csv
temp.to_csv(r'data/osudata.csv', index = False,mode='a', header=False)

