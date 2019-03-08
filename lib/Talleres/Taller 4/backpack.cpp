#include "backpack.h"

BackPack::BackPack(string nam, int lim)
{
    name = nam;
    limit = lim;
}

string BackPack::get_name()
{
    return name;
}

int BackPack::get_limit()
{
    return limit;
}