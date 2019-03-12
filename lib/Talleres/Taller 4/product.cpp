#include "product.h"

Product::Product()
{

}

Product::~Product()
{

}

Product::Product(string newCategory, string newName, int newPrice)
{
    category = newCategory;
    name = newName;
    price = newPrice;
}

string Product::get_category() const
{
    return category;
}

string Product::get_name() const
{
    return name;
}

int Product::get_price() const
{
    return price;
}