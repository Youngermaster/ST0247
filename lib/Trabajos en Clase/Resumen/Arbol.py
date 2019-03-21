#Busqueda en un arbol binario

import os

class node():
    def __init__(self, dato):
        self.izq = None
        self.der = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, subArbol, dato):
        if subArbol == None:
            subArbol = node(dato)
        else:
            d = subArbol.dato
            if dato < d:
                subArbol.izq = self.insert(subArbol.izq, dato)
            else:
                subArbol.der = self.insert(subArbol.der, dato)
        return subArbol

    def inorder(self, subArbol):
        if subArbol == None:
            return None
        else:
            self.inorder(subArbol.izq)
            print(subArbol.dato)
            self.inorder(subArbol.der)

    def preorder(self, subArbol):
        if subArbol == None:
            return None
        else:
            print(subArbol.dato)
            self.preorder(subArbol.izq)
            self.preorder(subArbol.der)

    def postorder(self, subArbol):
        if subArbol == None:
            return None
        else:
            self.postorder(subArbol.izq)
            self.postorder(subArbol.der)
            print(subArbol.dato)

    def buscar(self, dato, subArbol):
        if subArbol == None:
            return None
        else:
            if dato == subArbol.dato:
                return subArbol.dato
            else:
                if dato < subArbol.dato:
                    return self.buscar(dato, subArbol.izq)
                else:
                    return self.buscar(dato, subArbol.der)
#============================================================

#progrmaa
arbolDatos = arbol()

while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Salir \n\nElige una opcion -> ")

    if opc == '1':
        nodo = input("\nIngresa el nodo (valor numerico) -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            arbolDatos.root = arbolDatos.insert(arbolDatos.root, nodo)
        else:
            print("\nIngresa solo números...")

    elif opc == '2':
        if arbolDatos.root == None:
            print("Arbol de datos Vacio")
        else:
            arbolDatos.inorder(arbolDatos.root)

    elif opc == '3':
        if arbolDatos.root == None:
            print("Arbol de datos Vacio")
        else:
            arbolDatos.preorder(arbolDatos.root)

    elif opc == '4':
        if arbolDatos.root == None:
            print("Arbol de datos Vacio")
        else:
            arbolDatos.postorder(arbolDatos.root)

    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if arbolDatos.buscar(nodo, arbolDatos.root) == None:
                print("\nValor (Nodo) no encontrado en el arbol de datos...")
            else:
                print("\nValor (Nodo) encontrado en el arbol de datos -> ",arbolDatos.buscar(nodo, arbolDatos.root), " si existe...")
        else:
            print("\nIngresa solo números...")        
    elif opc == '6':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()