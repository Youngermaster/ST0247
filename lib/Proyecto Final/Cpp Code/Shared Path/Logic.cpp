#include "pch.h"
#include "Logic.h"

const int NUMBER_OF_NODES = 4;
const double TIME_RATE_CHANGE = 1.2;
int costMatrix[NUMBER_OF_NODES + 1][NUMBER_OF_NODES + 1];

Logic::Logic()
{
    core();
}

Logic::~Logic()
{
}

void Logic::core()
{
	auto start = std::chrono::system_clock::now(); // Starts to counting time.

	fillMatrix();
	std::cout << "NUMBER_OF_NODES: " << NUMBER_OF_NODES << " TIME_RATE_CHANGE: " << TIME_RATE_CHANGE << std::endl;
	readFile(NUMBER_OF_NODES, TIME_RATE_CHANGE);
	algorithm();

	auto end = std::chrono::system_clock::now(); // Finishes to counting time.
	std::chrono::duration<double> elapsed_seconds = end - start; // It calcs the execution time.
	std::cout << std::endl << "elapsed time: " << elapsed_seconds.count() << " seconds\n"; // Prints the execution time on seconds.
}

void Logic::readFile(const int NUMBER_OF_NODES, const double TIME_RATE_CHANGE)
{
	std::ifstream myReadFile;
	myReadFile.open("../Datasets/dataset-ejemplo-U=4-p=1.2.txt");
	
	std::string line;
	std::string id;
	std::string xCoord;
	std::string yCoord;
	std::string name;

	int lineNumber = 0;

	if (myReadFile.is_open())
	{
		while (!myReadFile.eof()) 
		{
			lineNumber++;

			if (lineNumber < 5 || lineNumber == NUMBER_OF_NODES + 6  || lineNumber == NUMBER_OF_NODES + 7)
			{
				myReadFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // skip bad input
				continue;
			}

			// We have to minus 1 if the NUMBER_OF_NODES is equal to 4 
			// 'cause the teacher did it bad.
			if (lineNumber >= 5 && lineNumber < NUMBER_OF_NODES + 6)
			{
				std::getline(myReadFile, id, ' ');
				std::getline(myReadFile, xCoord, ' ');
				std::getline(myReadFile, yCoord, ' ');
				std::getline(myReadFile, name, '\n');

				User newUser(id, name);

				users.push_back(newUser);
				
				continue;
			}

			if (lineNumber > NUMBER_OF_NODES + 7)
			{
				std::string begin;
				std::string end;
				std::string cost;

				std::getline(myReadFile, begin, ' ');
				std::getline(myReadFile, end, ' ');
				std::getline(myReadFile, cost, '\n');
			
				if (begin == "")
					break;

				if (begin == "1" || begin == "\n1")
				{
					users.at(std::stoi(end) - 1).setHeuristicValue(std::stoi(cost));
				}

				costMatrix[std::stoi(begin) - 1][std::stoi(end) - 1] = std::stoi(cost);
			}
		}
	}
	else
		std::cout << "ERROR: file open" << std::endl;
	
	myReadFile.close();
}

void Logic::algorithm()
{
	const int usersPerVehicle = 5;
	int maxTime = 0;
	int timeAcummulated = 0;
	int quantityOfPeopleOnCar = 0;
	int iterator = 0;
	
	// Sorts the users depending of their heuristic value.
	std::sort(users.begin(), users.end(), [](const auto& user1, const auto& user2)
	{	return user1.getHeuristicValue() > user2.getHeuristicValue();	});
	
	while (quantityOfPeopleOnCar != users.size())
	{
		// Detectamos si el usuario en la posición del iterador está montado en un carro.
		if (users.at(iterator).getOnCar())
		{
			iterator++;
			continue;
		}

		std::vector<User> car;
		int minimun = 1000;
		int auxuliaryIterator = iterator;
		int iteratorWithTheMinimumValue = iterator;

		while (auxuliaryIterator != -1)
		{
			if (car.size() <= usersPerVehicle)
			{
				car.push_back(users.at(auxuliaryIterator));
				users.at(auxuliaryIterator).setOnCar(true);
				quantityOfPeopleOnCar++;
			}

			for (int minimumIterator = 0; minimumIterator <= NUMBER_OF_NODES; minimumIterator++)
				if (minimun > costMatrix[std::stoi(users.at(auxuliaryIterator).getId())][minimumIterator]
					&& !users.at(minimumIterator).getOnCar()
					&& costMatrix[std::stoi(users.at(auxuliaryIterator).getId())][minimumIterator] != 0
					)
				{
					minimun = costMatrix[std::stoi(users.at(auxuliaryIterator).getId())][minimumIterator];
					iteratorWithTheMinimumValue = minimumIterator;
				}

			if (iteratorWithTheMinimumValue == 0)
			{
				iteratorWithTheMinimumValue = -1;
			}

			auxuliaryIterator = iteratorWithTheMinimumValue;
		}
		
		iterator++;

		std::cout << "\t ->";
		for (auto x : car)
			std::cout << x.getId() << " ";
	}
}

void Logic::fillMatrix()
{
	for (int rows = 0; rows <= NUMBER_OF_NODES; rows++)
		for (int columns = 0; columns <= NUMBER_OF_NODES; columns++)
			costMatrix[rows][columns] = 0;
}
/*
		1	2	3	4	5
	1	0	7	19	27	17
	2	7	0	12	15	10
	3	19	12	0	8	14
	4	27	15	8	0	10
	5	17	10	14	10	0
*/