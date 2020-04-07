#importing matplotlib
import matplotlib.pyplot as plt

#importing pandas
import pandas as pd 

#sets options for printing Pandas data
#pd.set_option("display.max_rows", None, "display.max_columns", None)

#sets df
df = pd.read_csv('data/osudata.csv')

################################################################################################

#def that takes day, returns df for single day
def testday(day):
    return df[df['day'] == day]

def mvpTerritories():
    return df[df['mvp'] == True]

################################################################################################
#MVP related (mvp)
#mvp = mvpTerritories()
#*prints each territory where an MVP was awarded as well as count of MVP's in that location
#print(mvp['territory'].value_counts())
#*prints each day as well as the number of MVP's for each territory*
#print(mvp.groupby('day')['territory'].value_counts())


################################################################################################
#single day related (single)
single = testday(14)
print(single['territory'].value_counts(normalize = True)*100)
#single['territory'].value_counts(normalize = True).plot(kind='bar')
#plt.show()
################################################################################################
#full dataset related (df)
#print(df['regularTeam'].value_counts())

################################################################################################
#Mapping related
################################################################################################
print("fin")