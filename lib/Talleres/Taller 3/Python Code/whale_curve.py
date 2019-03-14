import csv

datos1 = []
datos2 = []

def leerCSV(pathArchivo, datos):
    with open(pathArchivo, encoding='latin1') as datos_csv:
        lectura = csv.reader(datos_csv, delimiter=';')
        #no leer la cabecera: titulo de las columnas
        next(lectura, None)
        contadorReg = 0
#        datos = []
        for linea in lectura:
            #nombreProyecto = linea[4]
            #comuna = linea[5]
            #inversion = linea[7]
            #if contadorReg < 6637: #6637
            datos.append(linea[5])
            #elif contadorReg >= 6637:   
                #datos2.append(linea[5])
            #contadorReg += 1

def core():
    leerCSV('E:\GIT\Github Projects\ST0247\lib\Talleres\Taller 3\Python Code\MEData.1.csv', datos1)
    leerCSV('E:\GIT\Github Projects\ST0247\lib\Talleres\Taller 3\Python Code\MEData.2.csv', datos2)
    print(datos1)
    print(datos2)


if __name__ == "__main__":
    core()
