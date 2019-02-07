import 'dart:io';

/**
 *
 * returns a integer
 */
readDouble(String message) {
  print(message);
  var read = stdin.readLineSync().trim();
  return double.parse(read);
}
