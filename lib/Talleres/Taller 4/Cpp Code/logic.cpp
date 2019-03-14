#include "logic.h"

Logic::Logic() 
{
    this->proteins.set_name("Proteins");
    this->proteins.set_limit(50000);
    this->proteins.set_obligatory_elements(8);
    this->flour.set_name("Flour");
    this->flour.set_limit(50000);
    this->flour.set_obligatory_elements(10);
    this->grain.set_name("Grain");
    this->grain.set_limit(50000);
    this->grain.set_obligatory_elements(3);
    this->toiletries.set_name("Toiletries");
    this->toiletries.set_limit(50000);
    this->toiletries.set_obligatory_elements(4);
    this->oilsAndSauces.set_name("Oils and sauces");
    this->oilsAndSauces.set_limit(50000);
    this->oilsAndSauces.set_obligatory_elements(3);
    this->vegetables.set_name("Vegetables");
    this->vegetables.set_limit(50000);
    this->vegetables.set_obligatory_elements(12);
    this->optional.set_name("Optional");

    core();
}

Logic::~Logic() { }

void Logic::core()
{
    read_file("listacsv.csv");
    vector <Product> auxiliar = proteins.get_products();


    for(int iterator = 0; iterator < auxiliar.size(); iterator++)
        cout << "What's up?" << endl;
    
    
}

void Logic::read_file(string path)
{
    ifstream ip(path); // "listacsv.csv"

    if (!ip.is_open()) cout << "ERROR: file is already open." << endl;

    short int counter = 0;

    string category, name, price;
   
    while(ip.good())
    {
        if (counter == 0)
        {
            counter++;
            continue;
        }

        getline(ip, category, ';');
        getline(ip, name, ';');
        getline(ip, price, '\n');


        int newPrice = stoi(price);
        Product newProduct(category, name, newPrice);

        if (category == "Proteina")
            proteins.add_product(newProduct);
        else if (category == "Harina")
            flour.add_product(newProduct);
        else if (category == "Granos")
            grain.add_product(newProduct);
        else if (category == "Aseo")
            toiletries.add_product(newProduct);
        else if (category == "Aceite y salsa")
            oilsAndSauces.add_product(newProduct);
        else if (category == "Vegetales")
            vegetables.add_product(newProduct);
        else
            optional.add_product(newProduct);
    }

    ip.close();
}