#include "product.h"

Product::Product() { }

Product::~Product() { }

Product::Product(string newCategory, string newName, int newPrice)
{
    this->category = newCategory;
    this->name = newName;
    this->price = newPrice;
}

string Product::get_category() const { return category; }

string Product::get_name() const { return name; }

int Product::get_price() const { return price; }

void Product::set_category(string newCategory) { category = newCategory; }

void Product::set_name(string newName) { name = newName; }

void Product::set_price(int newPrice) { price = newPrice; }