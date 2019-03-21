colores = ['amarillo', 'morado', 'naranja','rojo', 'verde', 'azul' ]

nodos = ['Bra', 'Para', 'Chile', 'Arg', 'Bol', 
         'Uru', 'Guyana', 'GuiaF', 'Suriname','Trini','Col', 'Ven', 'Peru', 'Ecu' ]

aristas = {}
aristas['Col']=['Ven','Bra', 'Ecu', 'Peru']
aristas['Ven']=['Col','Bra','Trini','Guyana']
aristas['Peru']=['Col', 'Ecu', 'Bra', 'Bol', 'Chile']
aristas['Ecu']=['Col','Peru']
aristas['Bra']=['Col', 'Ven', 'Suriname','Guyana','GuiaF', 'Uru', 'Arg', 'Para','Bol','Peru']
aristas['Para']=['Bra', 'Arg', 'Bol']
aristas['Chile']=['Bol', 'Peru', 'Arg']
aristas['Arg']=['Bra', 'Uru', 'Chile', 'Para','Bol']
aristas['Bol']=['Para', 'Bra','Arg','Chile','Peru']
aristas['Uru']=['Arg', 'Bra']
aristas['Guyana']=['Ven','Bra', 'Suriname']
aristas['GuiaF']=['Bra', 'Suriname']
aristas['Suriname']=['GuiaF', 'Bra', 'Guyana']
aristas['Trini']=['Ven']

colores_de_nodos = {}

def validarColor(nodo, color):
    #print('ver pais:', nodo)
    #print('ver fronteras: ',aristas.get(nodo))
    for arista in aristas.get(nodo):
        color_de_arista = colores_de_nodos.get(arista)
        if color_de_arista == color:
            return False
    return True

def pintar_nodo(nodo):
    for color in colores:
        if validarColor(nodo, color):
            return color

def pintar():
    for nodo in nodos:
        colores_de_nodos[nodo] = pintar_nodo(nodo)

    for pais in colores_de_nodos:
        print(pais, ' : ', colores_de_nodos[pais])

pintar()





















