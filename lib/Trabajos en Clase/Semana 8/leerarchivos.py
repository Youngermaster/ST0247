
def leerCSV(pathArchivo):
    with open(pathArchivo, encoding='latin1') as datos_csv:
        lectura = csv.reader(datos_csv)
        #no leer la cabecera: titulo de las columnas
        next(lectura, None)
        contadorReg = 0
        datos = []
        for linea in lectura:
            #nombreProyecto = linea[4]
            #comuna = linea[5]
            #inversion = linea[7]
            datos.append([linea[4], linea[5], linea[7]])
            



