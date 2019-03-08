#include <iostream>
#include <fstream>

using namespace std;

void core();

int main(int argc, char const *argv[])
{
    core();
    return 0;
}

void core()
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