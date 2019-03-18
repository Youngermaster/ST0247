import csv
import operator

FIRST_BUDGET = 300000
SECOND_BUDGET = 200000

bill = 0

solutionBackPack = []
proteins = {}
flour = {}
grain = {}
toiletries = {}
oilsAndSauces = {}
vegetables = {}
optional = {}


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


def assign_limit_by_elements(list, limit):
    auxiliary_list = sorted(list.items(), key=operator.itemgetter(1))
    products = []
    prices = []

    global bill

    for iterator in range(len(auxiliary_list)):
        products.append(auxiliary_list[iterator][0])
        prices.append(auxiliary_list[iterator][1])

    iterator = 0

    while iterator < limit:
        if iterator == len(products):
            iterator = 0
            continue

        solutionBackPack.append(products[iterator])
        bill += prices[iterator]
        iterator += 1
    

def ultra_core(list, limit):
    auxiliary_list = sorted(list.items(), key=operator.itemgetter(1))
    products = []
    prices = []

    for iterator in range(len(auxiliary_list)):
        products.append(auxiliary_list[iterator][0])
        prices.append(auxiliary_list[iterator][1])
    
    itemWeight = []

    for i in range(len(products)):
        itemWeight.append(1)

    items = [itemWeight, prices]
    backpack(limit, items)

def backpack(maxWeight, items):
    matrix = [[0 for col in range(maxWeight+1)] for row in range(len(items[0]))]

    for row in range(len(items[0])):  # going through the matrix we set up
        for col in range(maxWeight+1):
            if items[0][row] > col:  # this is the check to see if the item can go into our knap-sack
                matrix[row][col] = matrix[row-1][col]  # get the item above and place
            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row-1][col-items[0][row]]+ items[1][row])
    for i in range(len(items[0])):
        print(matrix[i])
    packed = []
    col = maxWeight
    # checking to see which items will go into our knapsack
    for row in range(len(items[0])-1,-1,-1):
        if row == 0 and matrix[row][col] != 0:
            packed.insert(0,row)
        if matrix[row][col] != matrix[row-1][col]:
            packed.insert(0,row)
            col -= items[0][row]
    print(packed)
    print('Max value is ', matrix[len(items[0])-1][maxWeight])

def assign_optionals():
    auxiliary_list = sorted(optional.items(), key=operator.itemgetter(1))
    products = []
    prices = []

    global bill

    for iterator in range(len(auxiliary_list)):
        products.append(auxiliary_list[iterator][0])
        prices.append(auxiliary_list[iterator][1])


    while bill <= FIRST_BUDGET:
        if iterator < 0:
            break

        if iterator == len(products):
            iterator = 0
            continue

        if bill + prices[iterator] > FIRST_BUDGET:
            iterator -= 1
            continue

        solutionBackPack.append(products[iterator])
        bill += prices[iterator]
        iterator += 1




def core():
    read_csv('E:\GIT\Github Projects\ST0247\lib\Talleres\Taller 4\Python Code\listacsv.csv')
    assign_limit_by_elements(proteins, 8)
    assign_limit_by_elements(flour, 10)
    assign_limit_by_elements(grain, 3)
    assign_limit_by_elements(toiletries, 4)
    assign_limit_by_elements(oilsAndSauces, 3)
    assign_limit_by_elements(vegetables, 12)
    assign_optionals()
    print(solutionBackPack)
    print(bill)

if __name__ == "__main__":
    core()

