#imports everything
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

station_num=1
#opens the csvfile
with open('2016VizData.csv',newline ='') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',') 
    reader = csv.DictReader(csvfile)
    #makes a list of months
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    day_x = []
    for i in range(366):
        day_x.append(i)

    #creates the station class with 1 attribute
    class Station():
        def __init__(self,STID):
            self.STID= STID
            self.Maxlist = []
            self.minlist = []
            self.havglist = []
            self.wsmxlist = []

        def fill_list (self,row):
            if row['STID'] == self.STID:
                #TMAX list appending
                if float(row['TMAX']) != -996.00:
                    self.Maxlist.append(float(row['TMAX']))
                else:
                    self.Maxlist.append(self.Maxlist[-1])

                #TMIN list appending
                if float(row['TMIN']) != -996.00:
                    self.minlist.append(float(row['TMIN']))
                else:
                    self.minlist.append(self.minlist[-1])

                #HAVG list appending
                if float(row['HAVG']) != -996.00:
                    self.havglist.append(float(row['HAVG']))
                else:
                    self.havglist.append(self.havglist[-1])
                    
                #WSMX list appending
                if float(row['WSMX']) != -996.00:
                    self.wsmxlist.append(float(row['WSMX']))
                else:
                    self.wsmxlist.append(self.wsmxlist[-1])

    #creates stations and adds the names to a list
    ALTU = Station ("ALTU")
    BEAV = Station ("BEAV")
    TISH = Station ("TISH")
    NRMN = Station ("NRMN")
    TULN = Station ("TULN")
    stations = [BEAV,ALTU,NRMN,TISH,TULN]
    
    
    #fills station list
    for row in reader:
        for station in stations:
            station.fill_list(row)
            
    #user input
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
    Tmax_or_tmin_print = input("If you would like me to print only the Tmax type (1)\nif you would you like to see Tmin type (2)\nif you want to see the humity type (3)\nif you want to see only the rain totals type (4)")
    for station in stations:
        if Tmax_or_tmin_print == '1':
            plt.ylabel('Max Temperature(°F)')
            plt.plot(day_x, station.Maxlist)
        if Tmax_or_tmin_print == '2':
            plt.ylabel('Min Temperature(°F)')
            plt.plot(day_x, station.minlist)
        if Tmax_or_tmin_print == '3':
            plt.ylabel('Humidity')
            plt.plot(day_x, station.havglist)
        if Tmax_or_tmin_print == '4':
            plt.ylabel('rainfall')
            plt.plot(day_x, station.wsmxlist)

plt.xlabel('Days')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()