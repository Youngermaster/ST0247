#pragma once
#include <iostream>
#include <vector>
#include <string>

class User
{
public:
	User(std::string , std::string);
	~User();
	// Getters
	std::string getId() const;
	std::string getName() const;
	std::string getCarriedBy() const;
	std::vector<User> getCar() const;
	bool getOnCar() const;
	int getHeuristicValue() const;

	// Setters
	void setCarriedBy(std::string);
	void setOnCar(bool);
	void setHeuristicValue(int);

	bool addPassenger(User);

private:
	// It is the ID of the user.
	std::string id;
	// It is the name of the location of the user.
	std::string name;
	// If the user is carried by another person, this 'variable' will store
	// Its ID, otherwhise will be itself ID.
	std::string carriedBy;
	// This vector will store the people on the car.
	std::vector<User> car;
	// This bools show if the user is or isn't in a car.
	bool onCar;
	// This is the value from the user ubication to the node 1.
	int heuristicValue;
};