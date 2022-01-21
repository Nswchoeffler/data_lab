import csv
with open('BigData2016.csv',newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    ARD2maxTemp = 0.0
    ARD2minTemp = 150.0
    BEAVmaxTemp = 0.0
    BEAVminTemp = 150.0
    BOISmaxTemp = 0.0
    BOISminTemp = 150.0
    CENTmaxTemp = 0.0
    CENTminTemp = 150.0
    NRMNmaxTemp = 0.0
    NRMNminTemp = 150.0
    STILmaxTemp = 0.0
    STILminTemp = 150.0
    TISHmaxTemp = 0.0
    TISHminTemp = 150.0
    TULNmaxTemp = 0.0
    TULNminTemp = 150.0
    WOODmaxTemp = 0.0
    WOODminTemp = 150.0

    for row in reader:
        #ARD2
        if row['STID']== 'ARD2':
            if float(row['TMAX'])!= -996.00:
                if ARD2maxTemp < float(row['TMAX']):
                    ARD2maxTemp = float(row['TMAX'])
            if float(row['TMIN'])!= -996.00:
                if ARD2minTemp > float(row['TMIN']):
                    ARD2minTemp = float(row['TMIN'])
        #BEAV
        if row['STID']== 'BEAV':
            if float(row['TMAX'])!= -996.00:
                if BEAVmaxTemp < float(row['TMAX']):
                    BEAVmaxTemp = float(row['TMAX'])
            if float(row['TMIN'])!= -996.00:
                if BEAVminTemp > float(row['TMIN']):
                    BEAVminTemp = float(row['TMIN'])
        #Bois
        if row['STID']== 'BOIS':
            if float(row['TMAX'])!= -996.00:
                if BOISmaxTemp < float(row['TMAX']):
                    BOISmaxTemp = float(row['TMAX'])
            if float(row['TMIN'])!= -996.00:
                if BOISminTemp > float(row['TMIN']):
                    BOISminTemp = float(row['TMIN'])
        #CENT
        if row['STID']== 'CENT':
            if float(row['TMAX'])!= -996.00:
                if CENTmaxTemp < float(row['TMAX']):
                    CENTmaxTemp = float(row['TMAX'])
            if float(row['TMIN'])!= -996.00:
                if CENTminTemp > float(row['TMIN']):
                    CENTminTemp = float(row['TMIN'])
        #NRMN
        if row['STID']== 'NRMN':
            if float(row['TMAX'])!= -996.00:
                if NRMNmaxTemp < float(row['TMAX']):
                    NRMNmaxTemp = float(row['TMAX'])
            if float(row['TMIN'])!= -996.00:
                if NRMNminTemp > float(row['TMIN']):
                    NRMNminTemp = float(row['TMIN'])
        #STIL
        if row['STID']== 'STIL':
            if float(row['TMAX'])!= -996.00:
                if STILmaxTemp < float(row['TMAX']):
                    STILmaxTemp = float(row['TMAX'])
            if float(row['TMIN'])!= -996.00:
                if STILminTemp > float(row['TMIN']):
                    STILminTemp = float(row['TMIN'])
        #TISH
        if row['STID']== 'TISH':
            if float(row['TMAX'])!= -996.00:
                if TISHmaxTemp < float(row['TMAX']):
                    TISHmaxTemp = float(row['TMAX'])
            if float(row['TMIN'])!= -996.00:
                if TISHminTemp > float(row['TMIN']):
                    TISHminTemp = float(row['TMIN'])
        #TULN
        if row['STID']== 'TULN':
            if float(row['TMAX'])!= -996.00:
                if TULNmaxTemp < float(row['TMAX']):
                    TULNmaxTemp = float(row['TMAX'])
            if float(row['TMIN'])!= -996.00:
                if TULNminTemp > float(row['TMIN']):
                    TULNminTemp = float(row['TMIN'])
        #WOOD
        if row['STID']== 'WOOD':
            if float(row['TMAX'])!= -996.00:
                if WOODmaxTemp < float(row['TMAX']):
                    WOODmaxTemp = float(row['TMAX'])
            if float(row['TMIN'])!= -996.00:
                if WOODminTemp > float(row['TMIN']):
                    WOODminTemp = float(row['TMIN'])
    

    print(f"ARD2: Max:{ARD2maxTemp}, Min: {ARD2minTemp}")
    print(f"BEAV: Max:{BEAVmaxTemp}, Min: {BEAVminTemp}")
    print(f"BOIS: Max:{BOISmaxTemp}, Min: {BOISminTemp}")
    print(f"CENT: Max:{CENTmaxTemp}, Min: {CENTminTemp}")
    print(f"NRMN: Max:{NRMNmaxTemp}, Min: {NRMNminTemp}")
    print(f"STIL: Max:{STILmaxTemp}, Min: {STILminTemp}")
    print(f"TISH: Max:{TISHmaxTemp}, Min: {TISHminTemp}")
    print(f"TULN: Max:{TULNmaxTemp}, Min: {TULNminTemp}")
    print(f"WOOD: Max:{WOODmaxTemp}, Min: {WOODminTemp}")