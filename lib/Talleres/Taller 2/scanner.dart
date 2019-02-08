import 'dart:io';

/**
 *
 * returns a double.
 */
readDouble(String message) {
  print(message);
  var read = stdin.readLineSync().trim();
  return double.parse(read);
}


/**
 *
 * returns a integer.
 */
readInteger(String message) {
  print(message);
  var read = stdin.readLineSync().trim();
  return double.parse(read);
}
