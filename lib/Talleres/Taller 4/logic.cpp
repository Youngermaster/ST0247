#include "logic.h"

Logic::Logic() 
{
    proteins.set_name("Proteins");
    proteins.set_limit(50000);
    proteins.set_obligatory_elements(8);
    flour.set_name("Flour");
    flour.set_limit(50000);
    flour.set_obligatory_elements(10);
    grain.set_name("Grain");
    grain.set_limit(50000);
    grain.set_obligatory_elements(3);
    toiletries.set_name("Toiletries");
    toiletries.set_limit(50000);
    toiletries.set_obligatory_elements(4);
    oilsAndSauces.set_name("Oils and sauces");
    oilsAndSauces.set_limit(50000);
    oilsAndSauces.set_obligatory_elements(3);
    vegetables.set_name("Vegetables");
    vegetables.set_limit(50000);
    vegetables.set_obligatory_elements(12);
    optional.set_name("Optional");
}

Logic::~Logic() { }

void Logic::core()
{
    read_file("listacsv.csv");

    
    for(int iterator = 0; iterator < proteins.get_products.size(); iterator++)
    {
        cout << "What's up?" << endl;
    }
    
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