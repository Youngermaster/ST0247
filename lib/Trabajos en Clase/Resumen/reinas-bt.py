def Reinas(vectorSolucion,etapa,n):
	if etapa>=n:                             # si la etapa es mayor que n, entonces devolvemos falso para terminar
		return False
	exito = False                            # inicializamos exito a False como bandera
	
	while True:
            if (vectorSolucion[etapa] < n):                       # si el valor de la columna para la fila es mayor o igual que n, entonces no seguimos incrementando, con esto evitamos indices fuera del array.
                vectorSolucion[etapa] = vectorSolucion[etapa] + 1       # incrementamos el valor de columna para la reina i-esima de la fila i-esima.

            if (ValidarSolucion(vectorSolucion,etapa)):                    # si la reina i-esima de la fila i-esima de la columna j en la etapa k no entra en conflicto con otra reina, proseguimos.

                if etapa != n-1:                            # si aun no hemos acabado todas las etapas, procedemos a la siguiente etapa.
                    exito = Reinas(vectorSolucion, etapa+1,n)
                    if exito==False:                        # si del valor devuelto de Reinas tenemos falso, ponemos a 0 el valor de la etapa + 1 para asi descartar los nodos fracaso.
                        vectorSolucion[etapa+1] = 0
                else:
                    # print ('Solución: ',vectorSolucion) 
                    exito = True                            # si ya hemos acabado, devolvemos True.
            if (vectorSolucion[etapa]==n or exito==True):   # si el valor de la columna j de la etapa k es igual a n o exito es igual a True, salimos del bucle y devolvemos exito.
                break
	return exito


def ValidarSolucion(vectorSolucion,etapa):
	# Comprueba si el vectorSolucion construido hasta la etapa es 
	# prometedor, es decir, si la reina se puede situar en la columna de la etapa

	for i in range(etapa):
		if(vectorSolucion[i] == vectorSolucion[etapa]) or (compararAbs(vectorSolucion[i],vectorSolucion[etapa])==compararAbs(i,etapa)):
			return False

	return True

def compararAbs(x,y):
	if x>y:
		return x - y
	else:
		return y - x	



###############################

print ('-'*26)
print ('PROBLEMA DE LAS N - REINAS')
print ('-'*26)
n = int(input('Introduce el numero de reinas: '))

#crea el vectoSolucion en 0s
vectorSolucion = []
for i in range(n):               
	vectorSolucion.append(0)
etapa = 0

Reinas(vectorSolucion, etapa, n)
print ('Solución: ', vectorSolucion)