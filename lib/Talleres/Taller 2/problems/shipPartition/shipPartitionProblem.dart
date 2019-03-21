import '../../common/scanner.dart';
import '../../problem.dart';

class CargoShip implements Problem {

  @override
  bool available() => true;

  @override
  void call(args) => shipPartitionProblemCore(args[0]);
}

List _productList = List(); // This is the list of the products of the problem.
List _leftContainer = List(); // The left part of the ship container.
List _rightContainer = List(); // The right part of the ship container.

/**
 * The core of the problem
 * returns void.
 */
shipPartitionProblemCore(int products) {
  _addProducts(products);
  _bruteForce(_productList);
  _printFormatted();
}

/**
 * This method organize the output of the problem.
 * returns void.
 */
_printFormatted() {
  String ship = """
                        | ====
                        |   /
                        | /
                        |
   ********************************************
   |                    |                     |  
   |                    |                     |
   |       Right        |         Left        |
   |       Part         |         Part        |
   |                    |                     |
   |                    |                     |
   |                    |                     |
   |                    |                     |
   ********************************************
    \\                                       /
      \\                                    /
        \\                                /
          \\                            /
            \\                        /
              ***********************   
   """; // The structure of the ship.

  print("_" * 10);  // Prints ten times this line '_'.
  print("\nLeft part: ");
  _leftContainer.forEach((iterable) => print(iterable)); // Prints all the items of the list.
  print("* ${_getListsSum(_leftContainer)}"); // Prints the sum of all the elements of the list.
  print("_" * 10);  // Prints ten times this line '_'.
  print("Right part: ");
  _rightContainer.forEach((iterable) => print(iterable)); // Prints all the items of the list.
  print("* ${_getListsSum(_rightContainer)}"); // Prints the sum of all the elements of the list.
  print(ship); // Prints the structure of the ship.
}

/**
 * Adds all the products that you gave it.
 * returns void
 */
_addProducts(int amount) {
  int counter = 0;
  while (counter < amount) {
    double weight = readDouble("Enter the weight of the product, please: ");
    _productList.add(weight);
    counter++;
  }
}

/**
 * It is in charge of assign the weights to the right side.
 * returns void.
 */
_bruteForce(List list) {
  double balanceNumber = _getBalanceNumber(list); // The half number of the list of products
  mainLoop: for (int iterator = 0; iterator < list.length; iterator++) {
    _leftContainer.add(list[iterator]); // adds elements to the left container.
    // If the sum of all the elements is equal to the 'balanceNumber'.
    if (_getListsSum(_leftContainer) == balanceNumber) {
      // Add the rest of the elements in the list to the other side.
      _rightContainer = list.sublist(iterator++);
      // And if the other side is equal too the loop finish.
      if (_getListsSum(_rightContainer) == balanceNumber) {
        break mainLoop;
      }
      list.shuffle(); // Shuffle the list
      // Delete all the elements in the left side.
      _leftContainer.clear();
      iterator = 0; // Reset the iterator
      continue mainLoop;
    } else if( _getListsSum(_leftContainer) > balanceNumber) {
      list.shuffle();
      _leftContainer.clear();
      iterator = 0;
      continue mainLoop;
    }
  }
}

/**
 *  Obtains the sum of all the elements in the list.
 *  returns null if the list is empty else it will return all the sum.
 */
_getListsSum(List list) => list.isEmpty ? null : list.reduce((a, b) => a + b);


/**
 *  Obtains the half number.
 *  returns double.
 */
_getBalanceNumber(List list) => _getListsSum(list) / 2;