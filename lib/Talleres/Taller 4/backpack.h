#pragma once

#include "product.h"
#include <vector>

class BackPack
{
private:
    string name;
    int limit;
    vector <Product> products;
public:
    BackPack();
    BackPack(string newName, int newLimit);
    ~BackPack();
    string get_name() const;
    int get_limit() const;
    int get_total_products_price() const;
    vector<Product> get_products() const;
    void add_product(Product);
};
