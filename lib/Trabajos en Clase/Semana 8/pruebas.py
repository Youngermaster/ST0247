from Funciones import quicksort,mergesort
from Generadores import generarArrayInt
from time import time

a = generarArrayInt(10000000)
#print(a)

ti = time()
b = quicksort(a)
tf = time()-ti
print('quickSort tiempo: ', tf, ' seg')
#print('.....qs b:', b)

ti = time()
c = mergesort(a)
tf = time()-ti
print('mergeSort tiempo: ', tf, ' seg')
#print('.....ms c:', c)

ti = time()
d = sorted(a)
tf = time()-ti
print('Sort tiempo: ', tf, ' seg')
#print('.....bruejria d:', d)

