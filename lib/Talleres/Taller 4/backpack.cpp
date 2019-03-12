#include "backpack.h"

BackPack::BackPack() { }

BackPack::~BackPack() { }

BackPack::BackPack(string newName, int newLimit, int newObligatoryElements)
{
    name = newName;
    limit = newLimit;
    obligatoryElements = newObligatoryElements;
}

string BackPack::get_name() const { return name; }

int BackPack::get_limit() const { return limit; }

int BackPack::get_obligatory_elements() const { return obligatoryElements; }

int BackPack::get_total_products_price() const
{
    int sum = 0;
    for(int iterator = 0; iterator < products.size(); iterator++)
        sum += products[iterator].get_price();

    return sum;
}

vector <Product> BackPack::get_products() const { return products; }

void BackPack::add_product(Product& newProduct) { products.push_back(newProduct); }

void BackPack::set_name(string newName) { name = newName; }

void BackPack::set_limit(int newLimit) { limit = newLimit; }