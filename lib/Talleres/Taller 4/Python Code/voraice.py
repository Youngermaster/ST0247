import csv
import operator

proteins = {}
flour = {}
grain = {}
toiletries = {}
oilsAndSauces = {}
vegetables = {}
optional = {}

def leerCSV(pathArchivo):
    with open(pathArchivo, encoding='latin1') as datos_csv:
        lectura = csv.reader(datos_csv, delimiter=';')
        next(lectura, None)
        contadorReg = 0
        for line in lectura:
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

def core():
    leerCSV('E:\GIT\Github Projects\ST0247\lib\Talleres\Taller 4\Python Code\listacsv.csv')
    print("Proteins: {}".format(proteins))
    print("Flour: {}".format(flour))
    print("Grain: {}".format(grain))
    print("Toiletries: {}".format(toiletries))
    print("Oil and Sauces: {}".format(oilsAndSauces))
    print("Vegetables: {}".format(vegetables))
    print("Optionals: {}".format(optional))
    x = sorted(optional.items(), key = operator.itemgetter(1))
    print("\n\nOptionals: {}".format(x))
    for i in x:    
        print(i)

if __name__ == "__main__":
    core()
