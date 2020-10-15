#test.py

# from datetime import datetime

# date = datetime.now().strftime("%a %d/%m/%Y %I:%H:%M %p ")

# print(date)


import csv

def ReadData():
    with open('EP2\data.csv', newline='', encoding='utf-8') as file:
        fr = csv.reader(file)
        alldata = list(fr)
    return alldata

ReadData()