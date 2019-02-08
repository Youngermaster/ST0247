import 'dart:io';

/**
 * It gonna read a variable and if the variable have tabulations or line
 * spaces will trim they.
 * returns a double.
 */
readDouble(String message) {
  print(message);
  var read = stdin.readLineSync().trim();
  return double.parse(read);
}

/**
 * It gonna read a variable and if the variable have tabulations or line
 * spaces will trim they.
 * returns a integer.
 */
readInteger(String message) {
  print(message);
  var read = stdin.readLineSync().trim();
  return double.parse(read);
}