from time import time
from Generadores import generarArray
from MergeSort import *
from QuickSort import *

tamano = int(input("Cuantos números desea generar para ordenar? "))
a = generarArray(tamano)
#print('Array a: ', a)


start_time = time()
datosOrdenados = mergesort(a)
elapsed_time = time() - start_time
print("MSort Tiempo: %0.10f segundos." % elapsed_time)
#print('Array MSort: ', datosOrdenados)


start_time = time()
datosOrdenados = quicksort(a)
elapsed_time = time() - start_time
print("QSort Tiempo: %0.10f segundos." % elapsed_time)
#print('Array QSort: ', datosOrdenados)
