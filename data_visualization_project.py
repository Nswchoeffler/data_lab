#imports everything
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

station_num=1
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
    
    
    #fills station list
    for row in reader:
        for station in stations:
            station.fill_list(row)
            
    #user input
    user_name = input("what would you like me to call you?")
    print (f"Oh hello {user_name}!")
    certain_station_Y_N = input("would you like to see just one station? If so type 'Y' if not type 'N'")
    if certain_station_Y_N == "Y":
        for station in stations:
            print(f"({station_num}):{station.STID}")
            station_num +=1
        certain_station = input(" which one would you like to station. please type the station by number")
        for station in stations:
            plt.plot(day_x, stations[int(certain_station)-1].Maxlist, label = station.STID)
    if certain_station_Y_N == "N":
        for station in stations:
            plt.plot(day_x, station.Maxlist, label = station.STID)
    Tmax_or_tmin_print = input("If you would like me to print only the Tmax type (1)\n if you would you like me to only print the Tmin type (2)\n if you would like me to print both type (3)")





plt.xlabel('Days')
plt.ylabel('Temperature(°F)')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()