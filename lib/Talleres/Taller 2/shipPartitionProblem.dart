import 'scanner.dart';

main() {
  shipPartitionProblemCore();
}

List productList = List();
List _partOne = List();
List _partTwo = List();

/**
 * Core
 * returns void.
 */

shipPartitionProblemCore() {
  _addProducts(30);
  _bruteForce(productList);
  _printFormatted();
}

/**
 *
 * returns void.
 */

_printFormatted() {
  productList.forEach((iterable) => print(iterable));
  print("_" * 5);

  _partOne.forEach((iterable) => print(iterable));
  print("* ${_getListsSum(_partOne)}");
  print("_" * 5);
  _partTwo.forEach((iterable) => print(iterable));
  print("* ${_getListsSum(_partTwo)}");
}
/**
 *
 * returns void
 */
_addProducts(int amount) {
  int counter = 0;
  while (counter < amount) {
    double weight = readDouble("Enter the weight of the product, please: ");
    productList.add(weight);
    counter++;
  }
}

/**
 *
 * returns void.
 */
_bruteForce(List list) {
  double balanceNumber = _getBalanceNumber(list);
  mainLoop: for (int iterator = 0; iterator < list.length; iterator++) {
    _partOne.add(list[iterator]);
    if (_getListsSum(_partOne) == balanceNumber) {
      _partTwo = list.sublist(iterator++);
      if (_getListsSum(_partTwo) == balanceNumber) {
        break mainLoop;
      }
      list.shuffle();
      _partOne.clear();
      iterator = 0;
      continue mainLoop;
    } else if( _getListsSum(_partOne) > balanceNumber) {
      list.shuffle();
      _partOne.clear();
      iterator = 0;
      continue mainLoop;
    }
  }
}

/**
 *
 *  returns null if the list is empty else it will
 */
_getListsSum(List list) => list.isEmpty ? null : list.reduce((a, b) => a + b);


/**
 *
 *  returns double.
 */
_getBalanceNumber(List list) => _getListsSum(list) / 2;
