colores = ['Rojo', 'Azul', 'Verde', 'Amarillo', 'Morado', 'Naranaja']

nodos = ['Colombia', 'Venezuela', 'Peru', 'Ecuador', 'Brasil', 'Chile', 
        'Trinidad y Tobago','Guyana','Suriname','Guiana Francesa', 'Bolivia', 'Paraguay','Uruguay','Argentina']

aristas = {}
aristas['Colombia'] = ['Venezuela', 'Peru', 'Brasil', 'Ecuador']
aristas['Venezuela'] = ['Colombia', 'Brasil', 'Trinidad y Tobago','Guyana' ]
aristas['Trinidad y Tobago'] = ['Venezuela']
aristas['Guyana'] = ['Venezuela', 'Brasil', 'Suriname']
aristas['Suriname'] = ['Guyana', 'Brasil', 'Guiana Francesa']
aristas['Guiana Francesa'] = ['Suriname', 'Brasil']
aristas['Brasil'] = ['Venezuela', 'Colombia', 'Suriname', 'Guyana', 'Guiana Francesa', 'Uruguay', 'Paraguay','Bolivia','Argentina','Peru']
aristas['Uruguay'] = ['Argentina', 'Brasil']
aristas['Argentina'] = ['Uruguay', 'Brasil', 'Paraguiay', 'Bolivia','Chile']
aristas['Chile'] = ['Bolivia', 'Argentina', 'Peru']
aristas['Paraguay'] = ['Argentina', 'Brasil', 'Bolivia']
aristas['Peru'] = ['Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador']
aristas['Ecuador'] = ['Colombia', 'Peru']
aristas['Bolivia'] = ['Paraguay', 'Brasil', 'Argentina ', 'Chile', 'Peru']



colores_de_nodos = {}

def validarColor(nodo, color):
    for arista in aristas.get(nodo): 
        color_de_arista = colores_de_nodos.get(arista)
        if color_de_arista == color:
            #print("{} ya tiene color.".format(arista))
            return False

    return True

def pintar_nodo(nodo):
    for color in colores:
        if validarColor(nodo, color):
            return color

def main():
    for nodo in nodos:
        colores_de_nodos[nodo] = pintar_nodo(nodo)

    for pais in colores_de_nodos:
        print(pais,':',colores_de_nodos[pais])
    print (colores_de_nodos)


main()