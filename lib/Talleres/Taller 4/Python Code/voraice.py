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


def assign_limit_by_elements_first_budget(list, limit):
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
    

def assign_optionals_first_budget():
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


def menu():
    print("Estos son los productos que has pedido:\n")
    for i in solutionBackPack:
        print("-{}".format(i))
    print("\n -> La cuenta es: {}".format(bill))
    print("\n\tOh oh.")

    print("""                  xOOOOOOOkdoc;                                                           ,,:cloo:'
                  lOOOOOOOOOOOxoc;                                                    ,;cloxkOOOOl.
		   xOOOOOOOOOOOOOxoc;                                              ;:loxkOOOOOOOOk:
                   ck0OOOOO0OO00OOOOxl:                                       ,;codkO0OOOOOOOOOOOo'
                    ck0OOOOOOOOOOOOO0Okoc;                               :cloxOOOOOOOOOOOOOOOO00;
                     :xOOOOO0OOOOOOOOOOOkdc;                          cldkOOOOOOOOOOOOOOOOOOO0;
                      ;dO0OOOOO0OOOOOOOOOOkdodddxxxxkkkOOOOOOOOOOkkkxkkO0OOOOOOOOOOOOOOOOOOO0'
                       ,cxOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0000'
                         ,lkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0000;'
                           ,lkOOkxkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0000'
                            .;lodkO0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0000000;'
                              ;xOOOOOOOOOOOO0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO000000;'
                              dOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOko;
                             dOOOO0OOOxdoccxOO0OOOOOOOOOOOOOOOOOOOOxdoclxOOOOOOOOOOOo;
                            lOOOOOOOOoo00c.;xOOOOOOOOOOOOOOOOOOOOOll0O:.:k0OOOOOOOOOOo,
                           ckOOO0OO0Ol,::,.,d0OOOOOOOOOOOOOOOOOOOOc,::,.;x0OOOOOOOOOOkc'
                          ;dOOOOOOOO0kc,,,;oOOO0OO0OO0OOOOOOOOOOOOkc,,,:dOOOOOOOOOOOOOd,
                         ,lOOOOOOOOOOOOkxxkOOOOOOOOxdddkOOOOOOOOOOOOkxxOOOOOOOOOOOOOO0kc
                         ;xOOOkkkOOOOOOOOOOOOOOOOOxo:;:dOOOOOOOOOOOOOOOOOOOOkkkkOOOOOOOd;
                         ckxollllldkOOOOOOOOOOOOOO0OkkOOOOOOOOOOOOOOOOOOOkdlllllodkOOOOOc
                         odccccccccokOOOOOOOOOOOOOOO0OOOOOOOOO0OOOOOOOOOxlcccccccclk0OOOd;
                         ddcccccccclxOOOOOOOOOOOO            OOOOOOOOOOOdccccccccclx0OOOOl
                         xOdolclllokOOOOOOOOOOOO              OOOOOOOOOOkocccccccldOOOOOOd
			 lOOOkkkkOOOOOOOOOOOOOOO              OOOOOOOOOOOOkxdoddxkOOOOOOOOl
                          dOOOOOOOOOOOOOOOOOOOO0              OOOOOOOOOOOOOOOOOOOOOOOOOOOOd
                          cxOOOOOOOOOOOOOOOOOOOOOO           OOOOOOOOOOOOOOOOOOOOOOOOOOOOOk
                           cxOOOOOOOOOOOOOOOOOOOOOOOOO     OO0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
                            ck0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOx
    """)
    print("\n\tEl sistema de tarjeta no funciona :'(")
    


def core():
    read_csv('E:\GIT\Github Projects\ST0247\lib\Talleres\Taller 4\Python Code\listacsv.csv')
    assign_limit_by_elements_first_budget(proteins, 8)
    assign_limit_by_elements_first_budget(flour, 10)
    assign_limit_by_elements_first_budget(grain, 3)
    assign_limit_by_elements_first_budget(toiletries, 4)
    assign_limit_by_elements_first_budget(oilsAndSauces, 3)
    assign_limit_by_elements_first_budget(vegetables, 12)
    assign_optionals_first_budget()
    menu()
    
if __name__ == "__main__":
    core()

