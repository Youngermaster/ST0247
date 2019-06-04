import csv
from comuna import *
from matplotlib import pyplot as plt

name_of_comunas = set()
comunas = []


def read_csv(file_path):
    with open(file_path, encoding='latin1') as datos_csv:
        lecture = csv.reader(datos_csv, delimiter=';')
        next(lecture, None)
        list_counter = -1
        for line in lecture:
            if line[1] == "Comuna":
                if line[2] == "Suma Comunas":
                    continue
                if line[2] not in name_of_comunas:
                    list_counter += 1
                    new_comuna = Comuna(line[2])
                    comunas.append(new_comuna)
                    name_of_comunas.add(line[2])
                assign_people(comunas[list_counter], line[3], line[5], 'male')
                assign_people(comunas[list_counter], line[3], line[6], 'female')


def assign_people(comuna, age_range, people_quatity, gender):
    if age_range == ' 0-4' or age_range == ' 5-9':
        if gender == 'male':
            comuna.boys += int(people_quatity)

        else:
            comuna.girls += int(people_quatity)
    elif age_range == ' 10-14' or age_range == ' 15-19' or age_range == ' 20-24':
        if gender == 'male':
            comuna.young_men += int(people_quatity)
        else:
            comuna.young_women += int(people_quatity)
    elif age_range == ' 55-59' or age_range == ' 60-64' or age_range == ' 65-69' or \
         age_range == ' 70-74' or age_range == ' 75-79' or age_range == ' 80 Y MÁS':
        if gender == 'male':
            comuna.older_men += int(people_quatity)
        else:
            comuna.older_women += int(people_quatity)
    elif age_range == ' Total':
        if gender == 'male':
            comuna.men += int(people_quatity)
        else:
            comuna.women += int(people_quatity)


def draw(parameter_list):
    pass


def menu():
    print("\n(A). Densidad de la diferencia entre hombres y mujeres por comuna,\
            \npresentadola información de mayor diferencia a menor diferencia.")
    print("\n(B). Comuna según el número de infantes (personas menor a 10 años).\
           \n De mayora menor, para programas de primera infancia.")
    print("\n(C).Comuna según mujeres jóvenes (mujeres entre 10 años a 24 años).\
           \n De mayor a menor para programas de educación sexual.")
    print("\n(D).Comuna según adultos mayores (personas mayores a 55 años).\
           \n De mayor amenor para programas de tercera edad.")
    print("\n-> Seleccione una opción, si no desea ninguna opción digite cualquier cosa.\n")
    

def logic():
    x = []
    y = []
    auxiliar_comunas = comunas
    while True:
        print("\n\n")
        menu()
        option = input("Digite por favor: ")
        if option == 'a' or option == 'A':
            for iterator in auxiliar_comunas:
                iterator.difference_between_men_and_women = iterator.men - iterator.women
            
            auxiliar_comunas.sort(key=lambda x: x.difference_between_men_and_women, reverse=False)
            for iterator in auxiliar_comunas:
                y.append(iterator.difference_between_men_and_women)
                x.append(iterator.name)

            plt.plot(x, y, marker='o')
            plt.xlabel('Diferencia entre hombres y mujeres')
            plt.ylabel('Comuna')
            plt.title('Diferencia entre hombres y mujeres por comuna.')
            plt.show()
            x.clear()
            y.clear()
        elif option == 'b' or option == 'B':
            for iterator in auxiliar_comunas:
                iterator.childs = iterator.boys + iterator.girls

            auxiliar_comunas.sort(key=lambda x: x.childs, reverse=False)

            for iterator in auxiliar_comunas:
                y.append(iterator.childs)
                x.append(iterator.name)

            plt.plot(x, y, marker='o')
            plt.xlabel('infantes')
            plt.ylabel('Comuna')
            plt.title('Comuna según el número de infantes.')
            plt.show()
            x.clear()
            y.clear()
        elif option == 'c' or option == 'C':
            auxiliar_comunas.sort(key=lambda x: x.young_women, reverse=False)

            for iterator in auxiliar_comunas:
                y.append(iterator.young_women)
                x.append(iterator.name)

            plt.plot(x, y, marker='o')
            plt.xlabel('Mujeres jovenes')
            plt.ylabel('Comuna')
            plt.title('Comuna según mujeres jóvenes.')
            plt.show()
            x.clear()
            y.clear()
        elif option == 'd' or option == 'D':
            for iterator in auxiliar_comunas:
                iterator.olds = iterator.older_men + iterator.older_women

            auxiliar_comunas.sort(key=lambda x: x.olds, reverse=False)

            for iterator in auxiliar_comunas:
                y.append(iterator.olds)
                x.append(iterator.name)

            plt.plot(x, y, marker='o')
            plt.xlabel('Aldutos mayores')
            plt.ylabel('Comuna')
            plt.title('Comuna según adultos mayores.')
            plt.show()
            x.clear()
            y.clear()
        else:   
            break


def core():
    read_csv('PPMedellin2017.csv')
    logic()

if __name__ == "__main__":
    core()
