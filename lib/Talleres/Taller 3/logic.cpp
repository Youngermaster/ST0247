#include "logic.h"

Logic::Logic()
{
    core();
}

void Logic::core()
{
    int codigo_dependencia;
    string nombre_dependencia;
    int tipo_inversion;
    int codigo_BPIN;
    string nombre_proyecto;
    int codigo_comuna;
    map <int, int> codigo_comuna_cantidad_comuna;
    string nombre_comuna;
    float inversion;
    string ano;

    int counter = 0;
    ifstream ip("MEData.csv");
    if (!ip.is_open()) cout << "ERROR: file open" << endl;

    while(ip.good())
    {
        if (counter == 0)
        {
            counter++;
            continue;
        }
            
        getline(ip, codigo_dependencia, ';');
        getline(ip, nombre_dependencia, ';');
        getline(ip, tipo_inversion, ';');
        getline(ip, codigo_BPIN, ';');
        getline(ip, nombre_proyecto, ';');
        getline(ip, codigo_comuna, ';');
        getline(ip, nombre_comuna, ';');
        getline(ip, inversion, ';');
        getline(ip, ano, ';');
        
    }

    

    ip.close();
}

int main(int argc, char const *argv[])
{
    core();
    return 0;
}
