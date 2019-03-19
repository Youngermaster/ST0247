import csv

data = []
comunas = {'Popular': 0, 'Santa Cruz': 0, 'Manrique': 0, 'Aranjuez': 0, 'Castilla': 0, 'Doce de Octubre': 0,
           'Robledo': 0, 'Villa Hermosa': 0, 'Buenos Aires': 0, 'La Candelaria': 0, 'Laureles - Estadio': 0,
           'La América': 0, 'San Javier': 0, 'El Poblado': 0, 'Guayabal': 0, 'Belén': 0, 'San Sebastián de Palmitas': 0,
           'San Cristobal': 0, 'Altavista': 0, 'San Antonio de Prado': 0, 'Santa Elena': 0, 'Toda la Ciudad': 0}

def read_csv(pathArchivo):
    with open(pathArchivo, encoding='latin1') as data_csv:
        lecture = csv.reader(data_csv, delimiter=';')
        
        next(lecture, None)
        
        for line in lecture:
            data.append(line[5])


def funcname(parameter_list):
    pass


def paint(list):
    pass

def core():
    read_csv('MEData.csv')
    data.sort()
    print("\n ->{}".format(data))


if __name__ == "__main__":
    core()
