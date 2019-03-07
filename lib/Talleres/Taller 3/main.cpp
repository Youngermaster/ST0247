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

    int codigo_dependencia;
    string nombre_dependencia;
    int tipo_inversion;
    int codigo_BPIN;
    string nombre_proyecto;
    int codigo_comuna;
    string nombre_comuna;
    float inversion;
    string año;

    while(ip.good())
    {
        getline(ip, codigo_dependencia, '\n');
    }
    ip.close();


}