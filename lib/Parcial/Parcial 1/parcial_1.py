import csv
import operator
from comuna import *

bill = 0
second_bill = 0

name_of_comunas = set()
comunas = []


def read_csv(file_path):
    with open(file_path, encoding='latin1') as datos_csv:
        lecture = csv.reader(datos_csv, delimiter=';')
        next(lecture, None)
        for line in lecture:
            if line[1] == "Comuna":
                print("->")
                if line[2] in name_of_comunas:
                    pass
                else:
                    comunas.append(Comuna(line[2]))
                    name_of_comunas.add(line[2])

def assign_people(comuna, age_range, people_quatity, gender):
    if age_range == ' 0-4' or age_range == ' 5-9':
        if gender == 'male':
            comuna.boys += people_quatity
        else:
            comuna.girls += people_quatity    


def sum(parameter_list):
    pass


def draw(parameter_list):
    pass


def menu():
    pass
    

def core():
    read_csv('PPMedellin2017.csv')
    #menu()
    print("\n\n")
    #c = Comuna("Name")
    #c.boys = "Juan"
    #c.boys += " Manuel Young Hoyos"
    #print(c.boys)
    #print(c)



if __name__ == "__main__":
    core()
