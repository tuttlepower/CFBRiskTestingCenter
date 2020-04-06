import pandas as pd
import matplotlib.pyplot as plt
#https://www.dataquest.io/blog/excel-and-pandas/
#https://www.dataquest.io/blog/pandas-cheat-sheet/
excel_file = 'CFB/response_1585076760511.xlsx'
#json_file = 'CFB/response_1585076760511.json'
json_file = 'CFB/testJson.json'
land_excel = pd.read_excel(excel_file)
land_json = pd.read_json(json_file)
#print(land_excel["id"] +","+ land_excel["neighbors__id"])
#print(land_excel)
g = land_excel.groupby("id")["neighbors__id"]
print(g)
#create a new file
#f = open("id.csv", "x")

#create a new file
#g = open("neighbor.csv", "x")

#print({1},{2},land_excel.id,land_excel.neighbors__id)
#print(land_excel.neighbors__id
print("\n",land_excel.id,land_excel.neighbors__id)
#f.write("{0},{1},\n".format(land_excel.id,land_excel.neighbors__id))

#print(land_excel.neighbors__id)
    
#print(land_json)
#for id in land_json['id']:
#    print(id)
#    for neighbors in land_json["neighbors"]:
#        print(neighbors)
    