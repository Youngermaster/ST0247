#include "logic.h"

Logic::Logic()
{

}

Logic::~Logic()
{

}

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