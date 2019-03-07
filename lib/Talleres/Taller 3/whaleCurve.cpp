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
    ifstream ip("MEData.csv");
    if (!ip.is_open()) cout << "ERROR: file open" << endl;

    string codigo;
    string dependencia;
    string tipo_de_inversion;
    int codBPIN;

    while(ip.good()){
   
        getline(ip, proof, '\n');
    }
    ip.close();


}