#pragma once
#include "User.h"
#include <algorithm>
#include <chrono>
#include <ctime>
#include <fstream>


class Logic
{
public:
	Logic();
	~Logic();
private:
	void core();
	void readFile(const int, const double);
	void algorithm();
	void fillMatrix();
	std::vector<User> users;
};