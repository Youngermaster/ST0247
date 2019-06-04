#include "pch.h"
#include "User.h"

User::User(std::string newId, std::string newName)
{
	this->id = newId;
	this->name = newName;
	this->carriedBy = "";
	this->onCar = false;
	this->heuristicValue = 0;
}

User::~User()
{
}

/*
 * Getters
 */

std::string User::getId() const
{
	return this->id;
}

std::string User::getName() const
{
	return this->name;
}

std::string User::getCarriedBy() const
{
	return this->car.at(0).getName();
}

std::vector<User> User::getCar() const
{
	return this->car;
}

bool User::getOnCar() const
{
	return this->onCar;
}

int User::getHeuristicValue() const
{
	return this->heuristicValue;
}

/*
 * Setters
 */

void User::setCarriedBy(std::string carry)
{
	this->carriedBy = carry;
}

void User::setOnCar(bool status)
{
	this->onCar = status;
}

void User::setHeuristicValue(int hValue)
{
	this->heuristicValue = hValue;
}

bool User::addPassenger(User user)
{
	if (car.size() > 5)
		return false;

	car.push_back(user);
	return true;
}