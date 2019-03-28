import csv
import operator
from comuna import *

bill = 0
second_bill = 0




def read_csv(file_path):
    with open(file_path, encoding='latin1') as datos_csv:
        lecture = csv.reader(datos_csv, delimiter=';')
        next(lecture, None)
        for line in lecture:
            if line[0] == "Proteina":
                proteins[line[1]] = int(line[2])
            elif line[0] == "Harina":
                flour[line[1]] = int(line[2])
            elif line[0] == "Granos":
                grain[line[1]] = int(line[2])
            elif line[0] == "Aseo":
                toiletries[line[1]] = int(line[2])
            elif line[0] == "Aceite y salsa":
                oilsAndSauces[line[1]] = int(line[2])
            elif line[0] == "Vegetales":
                vegetables[line[1]] = int(line[2])
            else:
                optional[line[1]] = int(line[2])


def menu():
    pass
    

def core():
    #read_csv('PPMedellin2017.csv')
    #menu()
    print("\n\n")
    c = Comuna("Name")
    c.boys = "Juan"
    print(c.boys)



if __name__ == "__main__":
    core()
