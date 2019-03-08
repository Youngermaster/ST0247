#pragma once

#include <iostream>
#include <string>
#include <map>

using namespace std;

class Row
{
public:
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
private:
    Row(int c_d, string n_d, int t_i, int c_BPIN, string n_p,
        int c_c, string n_c, float i, string ano);
    ~Row();
    int get_codigo_dependencia();
    string get_nombre_dependencia();
    int get_tipo_inversion();
    int get_codigo_BPIN();
    string get_nombre_proyecto();
    int get_codigo_comuna();
    string get_nombre_comuna();
    float get_inversion();
    string get_ano();
};