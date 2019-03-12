#include "logic.h"

Logic::Logic() 
{
    proteins.set_name("Proteins");
    proteins.set_limit(50000);
    flour.set_name("Flour");
    flour.set_limit(50000);
    grain.set_name("Grain");
    grain.set_limit(50000);
    toiletries.set_name("Toiletries");
    toiletries.set_limit(50000);
    oilsAndSauces.set_name("Oils and sauces");
}

Logic::~Logic() { }

void Logic::core()
{
    ifstream ip("listacsv.csv");
    if (!ip.is_open()) cout << "ERROR: file open" << endl;

    string proof;
   /**
    while(ip.good())
    {
    }
   */
    getline(ip, proof, '\n');
    cout << proof << endl;
    ip.close();
}