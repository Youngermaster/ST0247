import 'scanner.dart';

main() {

  _addProducts(6);
  _chibchoGauss(_productList);
  //_swinging();

  _productList.forEach((iterable) => print(iterable.weight));
  print("_" * 5);
  _partOne.forEach((iterable) => print(iterable.weight));
  print("_" * 5);
  _partTwo.forEach((iterable) => print(iterable.weight));
}

List<Product> _productList = List();
List<Product> _partOne = List();
List<Product> _partTwo = List();


/**
 *
 *
 */
_getMiddle(List list) => _getListsSum(list) / 2;

/**
 *
 * returns void
 */
_addProducts(int amount) {
  int counter = 0;
  while (counter < amount) {
    double weight = readDouble("Enter the weight of the product ${counter + 1}, please: ");
    var newProduct = Product("Product ${counter + 1}", weight);
    _productList.add(newProduct);
    counter++;
  }
}

/**
 *
 *  returns void.
 */
_chibchoGauss(List<Product> list) {
  List weights = List();

  for (Product products in list)
      weights.add(products.weight);

  weights.sort();
  print(weights);
  int leftCounter;
  int rightCounter = list.length - 1;
  double halfNumber = _getMiddle(weights);

  var leftSum = 0.0;
  var rightSum = 0.0;

  if (list.length % 2 == 0) {
    for (leftCounter = 0; leftCounter < (list.length / 2) - 1; leftCounter += 2) {
      _partOne.add(list[leftCounter]);
      leftSum += weights[leftCounter];
      _partOne.add(list[rightCounter]);
      leftSum += weights[rightCounter];

      rightCounter -= 2;
    }

    rightCounter = list.length - 2;

    for (leftCounter = 1; leftCounter < (list.length / 2); leftCounter += 2) {
      _partTwo.add(list[leftCounter]);
      rightSum += weights[leftCounter];
      _partTwo.add(list[rightCounter]);
      rightSum += weights[rightCounter];

      rightCounter -= 2;
    }

    print(leftSum);
    print(rightSum);

    bool booleanOne = leftSum + weights[((list.length ~/2) - 1)] == halfNumber;
    bool booleanTwo = rightSum + weights[((list.length ~/2) - 1)] == halfNumber;
    bool booleanThree = rightSum + weights[(list.length ~/2)] == halfNumber;
    bool booleanFour = leftSum + weights[(list.length ~/ 2)] == halfNumber;
    if (booleanOne && booleanThree) {
      _partOne.add(list[list.indexOf(((weights.length ~/2) - 1))]);
      _partTwo.add(list[(list.length ~/2)]);
      print("I'm here");
    } else if(booleanTwo && booleanFour) {
      print("WTF!");
      _partOne.add(list[(list.length ~/2)]);
      _partTwo.add(list[((list.length ~/2) - 1)]);
    } else {
      print("There are not solution");
    }

  }

}

/**
 *
 * returns void.
 */
_swinging() {
  double weightRight = 0;
  double weightLeft = 0;

  for (Product product in _productList) {
    if (weightRight - product.weight >= weightLeft - product.weight) {
      _partOne.add(product);
      weightLeft += product.weight;
    }
    else {
      _partTwo.add(product);
      weightRight += product.weight;
    }
  }
}

/**
 *
 * returns double
 */
_getListsSum(List list) => list.reduce((a, b) => a + b);

/**
 * Class product
 * contains...
 */
class Product {
 String name;
 double weight;

 Product(this.name, this.weight);
}