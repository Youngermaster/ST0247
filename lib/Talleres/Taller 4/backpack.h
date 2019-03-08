#pragma once

#include <iostream>
#include <string>
#include <vector>
#include "row.h"

using namespace std;

class BackPack
{
private:
    string name;
    int limit;
    vector <Row> rows;
public:
    BackPack(string nam, int lim);
    ~BackPack();
    string get_name();
    int get_limit();
    void add_row();
};