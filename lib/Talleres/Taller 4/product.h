#pragma once

#include <iostream>
#include <string>

using namespace std;

class Product
{
public:
    Product();
    Product(string, string, int);
    ~Product();
    string get_category() const;
    string get_name() const;
    int get_price() const;
private:
    string category;
    string name;
    int price;
};
