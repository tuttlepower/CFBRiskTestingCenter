import pandas as pd 
import matplotlib.pyplot as plt

url = "https://collegefootballrisk.com/api/roll/log?season=2&day=36"
df = pd.read_json(url)
gf = []
for territory in df['territoryRolls']:
    gf.append(territory)
gf = pd.DataFrame(gf)

print(gf.sort_values(by='randomNumber', ascending=False))
print(gf['winner'].value_counts())
print(gf.groupby('winner')['randomNumber'].mean())
print(gf['randomNumber'].describe())

gf.plot(kind='hist')
plt.show()
