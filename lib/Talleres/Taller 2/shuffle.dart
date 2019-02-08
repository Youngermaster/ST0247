import 'dart:math';

/**
 * This method will shuffle a list.
 * returns a List
 */
shuffle(List list) {
  var random = Random();  // This

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