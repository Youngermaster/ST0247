#pragma once

#include "product.h"
#include <vector>

class BackPack
{
private:
    string name;
    int limit;
    int obligatoryElements;
    vector <Product> products;
public:
    BackPack();
    BackPack(string, int, int);
    ~BackPack();
    string get_name() const;
    int get_limit() const;
    int get_obligatory_elements() const;
    int get_total_products_price() const;
    vector<Product> get_products() const;
    void add_product(Product);
    void set_name(string);
    void set_limit(int);
    void set_obligatory_elements(int);
};
