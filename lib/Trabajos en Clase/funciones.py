
def quicksort(datos):
    if len(datos) <= 1:
        return datos
    else:
        pivote = datos[0]
        return quicksort([x for x in datos[1:] if x < pivote]) + \
               [pivote] + \
               quicksort([x for x in datos[1:] if x >= pivote])

def mergesort(datos):
    if len(datos) < 2:
        return datos
    else:
        resultado=[]
        mitad = len(datos)//2   #int(len(datos)/2)
        datosInf = mergesort(datos[:mitad])
        datosSup = mergesort(datos[mitad:])
        i=0
        j=0
        while i<len(datosInf) and j<len(datosSup):
            if datosInf[i] > datosSup[j]:
                resultado.append(datosSup[j])
                j+=1
            else:
                resultado.append(datosInf[i])
                i+=1
        resultado += datosInf[i:]
        resultado += datosSup[j:]
        return resultado





















