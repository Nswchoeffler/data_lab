#imports everything
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

with open('BigData2016.csv',newline ='') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',') 
    reader = csv.DictReader(csvfile)

    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    day_x = []
    for i in range(366):
        day_x.append(i)

    #creates the station class with 1 attribute
    class Station():
        def __init__(self,STID):
            self.STID= STID
            self.Maxlist = []

        def fill_list (self,row):
            if row['STID'] == self.STID:
                if float(row['TMAX']) != -996.00:
                    self.Maxlist.append(float(row['TMAX']))
                else:
                    self.Maxlist.append(self.Maxlist[-1])

    #creates stations and adds the names to a list
    ARD2 = Station ("ARD2")
    BEAV = Station ("BEAV")
    BOIS = Station ("BOIS")
    CENT = Station("CENT")
    NRMN = Station ("NRMN")
    STIL = Station ("STIL")
    TISH = Station ("TISH")
    TULN = Station("TULN")
    WOOD = Station("WOOD")
    stations = [ARD2,BEAV,BOIS,CENT,NRMN,STIL,TISH,TULN,WOOD]
    
    for row in reader:
        for station in stations:
            station.fill_list(row)
            
    for station in stations:
        plt.plot(day_x, station.Maxlist, label = station.STID)

plt.xlabel('Days')
plt.ylabel('Temperature(°F)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()