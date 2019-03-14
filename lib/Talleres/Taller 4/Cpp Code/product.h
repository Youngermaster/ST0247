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
    void set_category(string);
    void set_name(string);
    void set_price(int);
private:
    string category;
    string name;
    int price;
};
