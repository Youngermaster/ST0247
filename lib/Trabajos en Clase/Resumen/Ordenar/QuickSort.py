def quicksort(datos): 
    if len(datos) <= 1:
        return datos
    else:
        pivote = datos[0]
        return quicksort([x for x in datos[1:] if x < pivote]) + \
               [pivote] + \
               quicksort([x for x in datos[1:] if x >= pivote])