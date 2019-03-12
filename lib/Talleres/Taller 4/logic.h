#pragma once

#include "backpack.h"
#include <iostream>
#include <fstream>

using namespace std;

class Logic
{
private:
    BackPack proteins;
    BackPack flour;
    BackPack grain;
    BackPack toiletries;
    BackPack oilsAndSauces;
    BackPack vegetables;
    BackPack optional;
    vector <Product> finalSolution;
public:
    Logic();
    ~Logic();
    void read_file(string);
    void core();
    void brute_force(vector<Product> , int);
};