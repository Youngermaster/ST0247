from ArbolBinario import * 
from Persona import * 

import datetime

#Por fecha de nacimiento
#arbol = ArbolBinario(Persona("Edi", datetime.date(1972,4,18)), lambda x,y: x.fechaNacimiento > y.fechaNacimiento)

#Por nombre
arbol = ArbolBinario(Persona("Edi", datetime.date(1972,4,18)), lambda x,y: x.nombre > y.nombre)

agregarElemento(arbol, Persona("Hedi", datetime.date(1972,4,18)))
agregarElemento(arbol, Persona("Sofia", datetime.date(1984,12,1)))
agregarElemento(arbol, Persona("Io", datetime.date(1980,11,1)))
agregarElemento(arbol, Persona("Rafaella", datetime.date(1978,8,13)))
agregarElemento(arbol, Persona("Pedro", datetime.date(1982,4,29)))
agregarElemento(arbol, Persona("Gertrudiz", datetime.date(2011,11,2)))
agregarElemento(arbol, Persona("Tomas", datetime.date(2007,6,4)))

#funcion en el recorrido
def imprimir(elemento):
    print (elemento)

print ("")
print ("---[in-orden]------")
ejecutarInOrden(arbol, imprimir)

print ("")
print ("---[pre-orden]------")
ejecutarPreOrden(arbol, imprimir)

print ("")
print ("---[post-orden]------")
ejecutarPostOrden(arbol, imprimir)