import csv
with open('BigData2016.csv',newline = '') as csvfile:
    reader = csv.DictReader(csvfile)

    class Stations():
        def _init_(self, stid):
            self.stid = stid
            self.maxTemp = []
            self.minTemp = []
        
station_names=[]
for row in reader:
    currentStation = row['STID']
    i = 0
    if len(station_names)==0:
        station_names.append(Stations(currentStation))
    for station in station_names:
        i += 1
        if station.stid == currentStation:
            break
        else:
            if i >= len(station_names):
                station_names.append(Stations(currentStation))

          

for station in station_names:
    if float(row['TMAX'])!= -996.00:
        station.maxTemp = float(row['TMAX'])
    if float(row['TMIN'])!= -996.00:
        station.minTemp = float(row['TMIN'])
            
for i in range(len(station_objects)):
    print (f"the max for {station_names} is {max(station(maxTemp))}")
    print (f"the min for {station_names} is {min(station(minTemp))}")