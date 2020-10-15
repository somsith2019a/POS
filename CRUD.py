import csv

def ReadData(csvfile):
    with open(csvfile, newline='', encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        return data

def EditData(csvfile, row, quantity):
  
    alldata = ReadData(csvfile)
    print(alldata)
    alldata[row][3] = str(int(alldata[0][3]) - quantity )

    with open(csvfile, 'w', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerows(alldata)
        print(alldata)
        
if __name__ == "__main__":
    pass
# EditData('EP4/data.csv', 0, 1)
