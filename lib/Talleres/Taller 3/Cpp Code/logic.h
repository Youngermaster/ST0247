#pragma once 
#include <iostream>
#include <fstream>
#include <vector>
#include "row.h"

using namespace std;


class Logic
{
private:
    vector <Row> rows;
    int file_length;
public:
    Logic();
    ~Logic();
    void add_row();
    void accumulate();
    void core();
    void set_file_length(int number);
    int get_file_length();
};
