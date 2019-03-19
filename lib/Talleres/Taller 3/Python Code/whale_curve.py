import csv

datos = []
comunas = {'Popular', 'Santa Cruz', 'Manrique', 'Aranjuez', 'Castilla', 'Doce de Octubre',
           'Robledo', 'Villa Hermosa', 'Buenos Aires', 'La Candelaria', 'Laureles - Estadio',
           'La América', 'San Javier', 'El Poblado', 'Guayabal', 'Belén', 'San Sebastián de Palmitas',
           'San Cristobal', 'Altavista', 'San Antonio de Prado', 'Santa Elena', 'Toda la Ciudad'}

def leerCSV(pathArchivo):
    with open(pathArchivo, encoding='latin1') as datos_csv:
        lectura = csv.reader(datos_csv, delimiter=';')
        #no leer la cabecera: titulo de las columnas
        next(lectura, None)
        
        for linea in lectura:
            #nombreProyecto = linea[4]
            #comuna = linea[5]
            #inversion = linea[7]
            datos.append(linea[5])
        
def funcname(parameter_list):
    pass

def core():
    leerCSV('E:\GIT\Github Projects\ST0247\lib\Talleres\Taller 3\Python Code\MEData.csv')
    datos.sort()
    print("\n ->{}".format(datos))


if __name__ == "__main__":
    core()
