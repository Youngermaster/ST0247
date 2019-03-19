import csv

data = []

"""comunas = [{"Popular": 0, "Santa Cruz": 0, "Manrique": 0, "Aranjuez": 0, "Castilla": 0, "Doce de Octubre": 0,
            "Robledo": 0, "Villa Hermosa": 0, "Buenos Aires": 0, "La Candelaria": 0, "Laureles - Estadio": 0,
            "La América": 0, "San Javier": 0, "El Poblado": 0, "Guayabal": 0, "Belén": 0, "San Sebastián de Palmitas": 0,
            "San Cristobal": 0, "Altavista": 0, "San Antonio de Prado": 0, "Santa Elena": 0, "Toda la Ciudad": 0}]"""


comunas = [0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0]

def read_csv(pathArchivo):
    with open(pathArchivo, encoding="latin1") as data_csv:
        lecture = csv.reader(data_csv, delimiter=";")
        
        next(lecture, None)
        
        for line in lecture:
            data.append(line[5])


def accumulate(comunas, data):

    countersito = 0
    comuna_counter_1 = 0 
    comuna_counter_2 = 0 
    comuna_counter_3 = 0 
    comuna_counter_4 = 0
    comuna_counter_5 = 0 
    comuna_counter_6 = 0 
    comuna_counter_7 = 0
    comuna_counter_8 = 0 
    comuna_counter_9 = 0 
    comuna_counter_10 = 0 
    comuna_counter_11 = 0 
    comuna_counter_12 = 0 
    comuna_counter_13 = 0 
    comuna_counter_14 = 0
    comuna_counter_15 = 0 
    comuna_counter_16 = 0 
    comuna_counter_50 = 0 
    comuna_counter_60 = 0 
    comuna_counter_70 = 0 
    comuna_counter_80 = 0
    comuna_counter_90 = 0
    comuna_counter_99 = 0

    for item in data:
        if item == 1:
            comuna_counter_1 += 1
            comunas[0] = comuna_counter_1
        elif item == 2:
            comuna_counter_2 += 1
            comunas[1] = comuna_counter_2
        elif item == 3:
            comuna_counter_3 += 1
            comunas[2] = comuna_counter_3
        elif item == 4:
            comuna_counter_4 += 1
            comunas[3] = comuna_counter_4
        elif item == 5:
            comuna_counter_5 += 1
            comunas[4] = comuna_counter_5
        elif item == 6:
            comuna_counter_6 += 1
            comunas[5] = comuna_counter_6
        elif item == 7:
            comuna_counter_7 += 1
            comunas[6] = comuna_counter_7
        elif item == 8:
            comuna_counter_8 += 1
            comunas[7] = comuna_counter_8
        elif item == 9:
            comuna_counter_9 += 1
            comunas[8] = comuna_counter_9
        elif item == 10:
            comuna_counter_10 += 1
            comunas[9] = comuna_counter_10
        elif item == 11:
            comuna_counter_11 += 1
            comunas[10] = comuna_counter_11
        elif item == 12:
            comuna_counter_12 += 1
            comunas[11] = comuna_counter_12
        elif item == 13:
            comuna_counter_13 += 1
            comunas[12] = comuna_counter_13
        elif item == 14:
            comuna_counter_14 += 1
            comunas[13] = comuna_counter_14
        elif item == 15:
            comuna_counter_15 += 1
            comunas[14] = comuna_counter_15
        elif item == 16:
            comuna_counter_16 += 1
            comunas[15] = comuna_counter_16
        elif item == 50:
            comuna_counter_50 += 1
            comunas[16] = comuna_counter_50
        elif item == 60:
            comuna_counter_60 += 1
            comunas[17] = comuna_counter_60
        elif item == 70:
            comuna_counter_70 += 1
            comunas[18] = comuna_counter_70
        elif item == 80:
            comuna_counter_80 += 1
            comunas[19] = comuna_counter_80
        elif item == 90:
            comuna_counter_90 += 1
            comunas[20] = comuna_counter_90
        elif item == 99:
            comuna_counter_99 += 1
            comunas[21] = comuna_counter_99
        else:
            countersito += 1
    print(countersito)    

def paint(x, y):
    pass

def core():
    read_csv("MEData.csv")
    #data.sort()
    accumulate(comunas, data)
    print(comunas)
    


if __name__ == "__main__":
    core()
