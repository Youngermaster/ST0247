#include "backpack.h"

BackPack::BackPack()
{

}

BackPack::~BackPack()
{

}

BackPack::BackPack(string nam, int lim)
{
    name = nam;
    limit = lim;
}

string BackPack::get_name() const
{
    return name;
}

int BackPack::get_limit() const
{
    return limit;
}

int BackPack::get_total_products_price() const
{
    int sum = 0;
    for(int iterator = 0; iterator < products.size(); iterator++)
        sum += products[iterator].get_price();

    return sum;
}

vector <Product> BackPack::get_products() const
{
    return products;
}

void BackPack::add_product(Product newProduct)
{
    products.push_back(newProduct);
}