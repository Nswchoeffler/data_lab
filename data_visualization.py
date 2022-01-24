import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class Station():
    def __init__(self,STID,MAXlist):
        self.STID= STID
        self.Maxlist = MAXlist

    def fill_list (self):
        if row['STID'] == self.STID:
            self.Maxlist.append(row['STID'])

ARD2 = Station ("ARD2", [])
BEAV = Station ("BEAV",[])
BOIS = Station ("BOIS", [])
CEMT = Station("CEMT",[])
NRMN = Station ("NRMN", [])
STIL = Station ("STIL",[])
TISH = Station ("TISH", [])
TULN = Station("TULN",[])
WOOD = Station("Wood", [])

stations = [ARD2,BEAV,BOIS,CEMT,NRMN,STIL,TISH,TULN,WOOD]

x = []
y = []
  
with open('BigData2016.csv',newline ='') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    reader = csv.DictReader(csvfile)
    for row in reader:
        for station in stations:
            station.fill_list(row)
            
    for row in plots:
        if row[4]!= -996.00:
            y.append(row[4])

        x.append(2)
        
        
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',marker = 'o',label = "Weather Data")
  
plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Temperature(°F)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()