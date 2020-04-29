import pandas as pd 
import matplotlib.pyplot as plt

rolls = pd.read_csv('D:/Github/CFBRiskTestingCenter/data/rolls.csv')
stars = pd.read_csv('D:/Github/CFBRiskTestingCenter/data/territory_info.csv')

#print(rolls.sort_values(by='randomNumber', ascending=False))
#print(rolls['winner'].value_counts())
#print(rolls.groupby('winner')['randomNumber'].mean())
#print(rolls['randomNumber'].describe())

#rolls.plot(kind='hist')
#plt.show()
print(rolls.shape)
#print(stars.head())

test = pd.merge(rolls,stars,on=['territory','day','winner'])
test['randint']= (test['randomNumber']/test['power'])
print(test.shape)
print(test.head())
#test.to_csv('test.csv',index=False)
#print(test['randint'].describe())
#test.groupby("", sort=False)["last_name"].count()
print(test.groupby('winner')['randint','players','power','randomNumber'].mean())

#test.groupby('winner')['randint'].plot(kind='hist',alpha=0.3)
plt.bar(test['winner'],test['randint'].mean())
plt.legend(loc='lower left')
plt.show()