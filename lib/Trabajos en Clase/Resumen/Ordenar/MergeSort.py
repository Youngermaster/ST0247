def mergesort(datos):
    if len(datos) < 2:
        return datos
    resultado = []
    mitad = int(len(datos) / 2)
    datosInf = mergesort(datos[:mitad])
    datosSup = mergesort(datos[mitad:])
    i = 0
    j = 0
    while i < len(datosInf) and j < len(datosSup):
        if datosInf[i] > datosSup[j]:
            resultado.append(datosSup[j])
            j += 1
        else:
            resultado.append(datosInf[i])
            i += 1
    resultado += datosInf[i:]
    resultado += datosSup[j:]
    return resultado

