import csv

datos1 = []
datos2 = []
datos3 = []

def leerCSV(pathArchivo, datos):
    with open(pathArchivo, encoding='latin1') as datos_csv:
        lectura = csv.reader(datos_csv, delimiter=';')
        #no leer la cabecera: titulo de las columnas
        next(lectura, None)
        
        for linea in lectura:
            #nombreProyecto = linea[4]
            #comuna = linea[5]
            #inversion = linea[7]
            datos.append(linea[5])


def core():
    leerCSV('E:\GIT\Github Projects\ST0247\lib\Talleres\Taller 3\Python Code\MEData_1.csv', datos1)
    leerCSV('E:\GIT\Github Projects\ST0247\lib\Talleres\Taller 3\Python Code\MEData_2.csv', datos2)
    #leerCSV('E:\GIT\Github Projects\ST0247\lib\Talleres\Taller 3\Python Code\MEData_3.csv', datos3)
    print("\n ->{}".format(datos1))
    print("\n ->{}".format(datos2))
    print("\n ->{}".format(datos3))


if __name__ == "__main__":
    core()
