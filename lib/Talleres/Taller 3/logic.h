#include <iostream>
#include <fstream>
#include <vector>
#include "row.h"

using namespace std;


class Logic
{
private:
    vector <Row> rows;
public:
    Logic();
    ~Logic();
    void add_row();
    void accumulate();
    void core();
};
