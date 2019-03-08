#include <iostream>
#include "row.h"

using namespace std;

Row::Row(int c_d, string n_d, int t_i, int c_BPIN, string n_p,
         int c_c, string n_c, float i, string ano)
{
  codigo_dependencia = c_d;
  nombre_dependencia = n_d;
  tipo_inversion = t_i;
  codigo_BPIN = c_BPIN;
  nombre_proyecto = n_p;
  codigo_comuna = c_c;
  nombre_comuna = n_c;
  inversion = i;
  ano = ano;
}

int Row::get_codigo_dependencia()
{
    return codigo_dependencia;
}

string Row::get_nombre_dependencia()
{
    return nombre_dependencia;
}

int Row::get_tipo_inversion()
{
    return tipo_inversion;
}

int Row::get_codigo_BPIN()
{
    return codigo_BPIN;
}

string Row::get_nombre_proyecto()
{
    return nombre_proyecto;
}

int Row::get_codigo_comuna()
{
    return codigo_comuna;
}

string Row::get_nombre_comuna()
{
    return nombre_comuna;
}

float Row::get_inversion()
{
    return inversion;
}

string Row::get_ano()
{
    return ano;
}