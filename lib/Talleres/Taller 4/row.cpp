#include "row.h"

Row::Row(string cat, string prod, int pr)
{
    categoria = cat;
    producto = prod;
    precio = pr;
}

string Row::get_categoria()
{
    return producto;
}

int Row::get_precio()
{
    return precio;
}

