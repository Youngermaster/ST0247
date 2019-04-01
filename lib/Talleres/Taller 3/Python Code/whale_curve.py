import csv
import re
from comuna import *
from matplotlib import pyplot as plt

popular = Comuna("Popular")
santa_cruz = Comuna("Santa Cruz")
manrique = Comuna("Manrique")
aranjuez = Comuna("Aranjuez")
castilla = Comuna("Castilla")
doce_de_octubre = Comuna("Doce de Octubre")
robledo = Comuna("Robledo")
villa_hermosa = Comuna("Villa Hermosa")
buenos_aires = Comuna("Buenos Aires")
la_candelaria = Comuna("La Candelaria")
laureles_estadio = Comuna("Laureles - Estadio")
la_america = Comuna("La América")
san_javier = Comuna("San Javier")
el_poblado = Comuna("El Poblado")
guayabal = Comuna("Guayabal")
belen = Comuna("Belén")
san_sebastian_de_palmitas = Comuna("San Sebastián de Palmitas")
san_cristobal = Comuna("San Cristobal")
altavista = Comuna("Altavista")
san_antonio_de_prado = Comuna("San Antonio de Prado")
santa_elena = Comuna("Santa Elena")
all_the_city = Comuna("Toda la Ciudad")

def read_csv(pathArchivo):
    with open(pathArchivo, encoding = "latin1") as data_csv:
        lecture = csv.reader(data_csv, delimiter = ";")
        next(lecture, None)

        for row in lecture:
            if row[6] == "Popular":
                assing_inversion_to_comuna(popular, row[7])
            elif row[6] == "Santa Cruz":
                assing_inversion_to_comuna(santa_cruz, row[7])
            elif row[6] == "Manrique":
                assing_inversion_to_comuna(manrique, row[7])
            elif row[6] == "Aranjuez":
                assing_inversion_to_comuna(aranjuez, row[7])
            elif row[6] == "Castilla":
                assing_inversion_to_comuna(castilla, row[7])
            elif row[6] == "Doce de Octubre":
                assing_inversion_to_comuna(doce_de_octubre, row[7])
            elif row[6] == "Robledo":
                assing_inversion_to_comuna(robledo, row[7])
            elif row[6] == "Villa Hermosa":
                assing_inversion_to_comuna(villa_hermosa, row[7])
            elif row[6] == "Buenos Aires":
                assing_inversion_to_comuna(buenos_aires, row[7])
            elif row[6] == "La Candelaria":
                assing_inversion_to_comuna(la_candelaria, row[7])
            elif row[6] == "Laureles - Estadio":
                assing_inversion_to_comuna(laureles_estadio, row[7])
            elif row[6] == "La América":
                assing_inversion_to_comuna(la_america, row[7])
            elif row[6] == "San Javier":
                assing_inversion_to_comuna(san_javier, row[7])
            elif row[6] == "El Poblado":
                assing_inversion_to_comuna(el_poblado, row[7])
            elif row[6] == "Guayabal":
                assing_inversion_to_comuna(guayabal, row[7])
            elif row[6] == "Belén":
                assing_inversion_to_comuna(belen, row[7])
            elif row[6] == "San Sebastián de Palmitas":
                assing_inversion_to_comuna(san_sebastian_de_palmitas, row[7])
            elif row[6] == "San Cristobal":
                assing_inversion_to_comuna(san_cristobal, row[7])
            elif row[6] == "Altavista":
                assing_inversion_to_comuna(altavista, row[7])
            elif row[6] == "San Antonio de Prado":
                assing_inversion_to_comuna(san_antonio_de_prado, row[7])
            elif row[6] == "Santa Elena":
                assing_inversion_to_comuna(santa_elena, row[7])
            elif row[6] == "Toda la Ciudad":
                assing_inversion_to_comuna(all_the_city, row[7])


def assing_inversion_to_comuna(comuna, inversion):
    inversion_splitted = re.split(",", inversion[1:]) # Erase the '$' in the inversion.
    inversion = ""

    for item in inversion_splitted: # Concat all the numbers splitted previously.
        inversion += item
    comuna.inversion = int(inversion)


def draw():
    comunas = [popular, santa_cruz, manrique, aranjuez, castilla,
               doce_de_octubre, robledo, villa_hermosa, el_poblado,
               la_candelaria, laureles_estadio, la_america,
               guayabal, belen, san_sebastian_de_palmitas,
               san_cristobal, altavista, san_antonio_de_prado,
               santa_elena, buenos_aires, san_javier, 
               all_the_city]
    x = []
    y = []
    comunas.sort(key=lambda x: x.inversion, reverse=False)

    for iterator in range(len(comunas)):
        if iterator > 1:
            comunas[iterator].inversion += comunas[iterator - 1].inversion
        
        y.append(comunas[iterator].inversion)
        x.append(comunas[iterator].name)

    plt.plot(x, y, marker='o')
    plt.xlabel('Inversion')
    plt.ylabel('Comunas')
    plt.title('Inversión acumulada por comuna en el año 2017.')
    plt.show()


def core():
    read_csv("MEData.csv")
    draw()


if __name__ == "__main__":
    core()
