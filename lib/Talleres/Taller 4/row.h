#pragma once

#include <iostream>
#include <string>

using namespace std;

class Row
{
public:
    string categoria;
    string producto;
    int precio;
private:
    Row(string cat, string prod, int pr);
    ~Row();
    string get_categoria();
    string get_producto();
    int get_precio();
};