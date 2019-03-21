import '../../common/shuffle.dart';
import '../../problem.dart';

class NumberFourteen implements Problem {

  @override
  bool available() => true;

  @override
  void call(args) => _coreNumberFourteen(args[0]);

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
    shuffle(firstNineNumbers);    // This method shuffle the list.
    // These methods will assign the values of the first nine numbers to the sectors.
    _assignValuesToSector(sectorNumberOne, firstNineNumbers[0], firstNineNumbers[1], firstNineNumbers[2]);
    _assignValuesToSector(sectorNumberTwo, firstNineNumbers[2], firstNineNumbers[3], firstNineNumbers[4]);
    _assignValuesToSector(sectorNumberThree, firstNineNumbers[2], firstNineNumbers[5], firstNineNumbers[6]);
    _assignValuesToSector(sectorNumberFour, firstNineNumbers[7], firstNineNumbers[6], firstNineNumbers[8]);

      // It Checks if all the sectors sums 14.
      if (_checkFourteenSum(sectorNumberOne) == false)
        continue;
      if (_checkFourteenSum(sectorNumberTwo) == false)
        continue;
      if (_checkFourteenSum(sectorNumberThree) == false)
        continue;
      if (_checkFourteenSum(sectorNumberFour) == false)
        continue;

      _printListFormatted();
      counter++;
    }
  }

  /**
   * This method will check if the sum of the elements of the list is 14.
   * returns a bool.
   */
  _checkFourteenSum(List<int> list) =>
      list.reduce((a, b) => a + b) == 14 ? true : false;

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
    print("_" * 11);
    print("| ${firstNineNumbers[0]}      ${firstNineNumbers[4]} |");
    print("|  ${firstNineNumbers[1]}   ${firstNineNumbers[3]}   |");
    print("|    ${firstNineNumbers[2]}     |");
    print("|    ${firstNineNumbers[5]}     |");
    print(
        "| ${firstNineNumbers[7]}  ${firstNineNumbers[6]}  ${firstNineNumbers[8]}  |");
    print("_" * 11);
  }