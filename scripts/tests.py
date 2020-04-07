import pandas as pd
import matplotlib.pyplot as plt
#https://www.dataquest.io/blog/excel-and-pandas/
#https://www.dataquest.io/blog/pandas-cheat-sheet/

pd.set_option("display.max_rows", None, "display.max_columns", None)

#url = 'https://collegefootballrisk.com/api/territories?season=2&day=14'

url = 'https://collegefootballrisk.com/api/team/odds?season=2&day=14&team=Ohio%20State'
df = pd.read_json(url)
print(df)