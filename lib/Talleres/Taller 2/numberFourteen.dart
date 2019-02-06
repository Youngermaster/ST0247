import 'dart:math';

main() {
  _coreNumberFourteen(1);
}

/**
 * This gonna be the structure of the solutions.
 * 0      4
 *  1   3
 *    2
 *    5
 *  7 6 8
 *  There will be four sectors for the solution to the problem.
 */
List<int> sectorNumberOne = List(3);    // 0, 1, 2
List<int> sectorNumberTwo = List(3);    // 2, 3, 4
List<int> sectorNumberThree = List(3);  // 2, 5, 6
List<int> sectorNumberFour = List(3);   // 7, 6, 8
// This is the list of the first nine number in the integers.
List<int> firstNineNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];

/**
 * This is the core of the problem.
 * returns void
 */
_coreNumberFourteen(int numberOfSolutions) {
  int counter = 0;
  while (counter < numberOfSolutions) {
    _shuffle(firstNineNumbers);
    _assignValuesToSector(sectorNumberOne, firstNineNumbers[0], firstNineNumbers[1], firstNineNumbers[2]);
    _assignValuesToSector(sectorNumberTwo, firstNineNumbers[2], firstNineNumbers[3], firstNineNumbers[4]);
    _assignValuesToSector(sectorNumberThree, firstNineNumbers[2], firstNineNumbers[5], firstNineNumbers[6]);
    _assignValuesToSector(sectorNumberFour, firstNineNumbers[7], firstNineNumbers[6], firstNineNumbers[8]);
    if (_checkFourteenSum(sectorNumberOne) == false)
      continue;
    if (_checkFourteenSum(sectorNumberTwo) == false)
      continue;
    if (_checkFourteenSum(sectorNumberThree) == false)
      continue;
    if (_checkFourteenSum(sectorNumberFour) == false)
      continue;

    print(firstNineNumbers);
    counter++;
  }
}

/**
 * This method will shuffle a list.
 * returns a List
 */
_shuffle(List list) {
  var random = Random();

  // Go through all elements.
  for (var iterator = (list.length - 1); iterator > 0; iterator--) {
    // Pick a pseudo random number according to the list length.
    var randomNumber = random.nextInt(iterator + 1);

    var temporalAuxiliaryNumber = list[iterator];
    list[iterator] = list[randomNumber];
    list[randomNumber] = temporalAuxiliaryNumber;
  }
  return list;
}

/**
 * This method will check if the sum of the elements of the list is 14.
 * returns a bool.
 */
_checkFourteenSum(List<int> list) => list[0] + list[1] + list[2] == 14 ? true : false;

/**
 * This method will assign three values to a sector (list).
 * returns void.
 */
_assignValuesToSector(List<int> sector, int value1, int value2, int value3) {
  sector[0] = value1;
  sector[1] = value2;
  sector[2] = value3;
}

/**
 * This method will prints the list of the solutions formatted.
 * returns void.
 */
_printListFormatted() {
  
}