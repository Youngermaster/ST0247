//import 'package:taller2datos/taller2datos.dart' as taller2datos;

import 'dart:io';

import 'problems/horse/horse.dart';
import 'problems/nqueen/nqueen.dart';
import 'problems/numberFourteen/numberFourteen.dart';
import 'problems/shipPartition/shipPartitionProblem.dart';

main(List<String> arguments) {

  print('[TALLER2] Escribe el numero del ejercicio para ejecutar:\n');

  print("(#1) REINAS NxN");
  print("(#2) CABALLO NxN");
  print("(#3) NUMERO 14");
  print("(#4) BARCO CARGUERO");

  var input = stdin.readLineSync();

  switch(input) {

    case '1':

      print('[REINAS] Escribe el tamaño del tablero NxN:\n');
      input = stdin.readLineSync();

      int value = int.tryParse(input);
      print('[REINAS] Tamaño del tablero \n' + value.toString() + 'x' + value.toString() + ' fijado.');
      print('[REINAS] ¿Fijar tres reinas? y/n');
      input = stdin.readLineSync();
      
      if(input.contains("y")) {

        print('[REINAS] Coloca el valor de la posición de A y luego la Columna de A.');

        int positionA = int.tryParse(stdin.readLineSync());
        int columnA   = int.tryParse(stdin.readLineSync());

        print('[REINAS] Coloca el valor de la posición de B y luego la Columna de B.');

        int positionB = int.tryParse(stdin.readLineSync());
        int columnB   = int.tryParse(stdin.readLineSync());

        print('[REINAS] Coloca el valor de la posición de C y luego la Columna de C.');

        int positionC = int.tryParse(stdin.readLineSync());
        int columnC   = int.tryParse(stdin.readLineSync());

        print('[REINAS] Generando ubicaciones posibles con 3 reinas predefinidas...');

        NQueen nQueen = NQueen();
        nQueen.call([true, value, [[positionA, columnA], [positionB, columnB], [positionC, columnC]]]);
        return;

      }

      print('[REINAS] Generando ubicaciones posibles...');

      NQueen nQueen = NQueen();
      nQueen.call([false, value]);
      return;

    case '2':

      print('[CABALLO] Escribe el tamaño del tablero NxN:\n');
      input = stdin.readLineSync();

      int value = int.tryParse(input);
      print('[CABALLO] Tamaño del tablero \n' + value.toString() + 'x' + value.toString() + ' fijado.');
      print('[CABALLO] Generando camino del caballo...');

      Horse horse = Horse();
      horse.call([value]);
      return;

    case '3':
      print('[NUMERO 14] Escribe el número de soluciones que desea tener:');
      input = stdin.readLineSync();
      int value = int.tryParse(input);

      NumberFourteen numberFourteen = NumberFourteen();
      numberFourteen.call([value]);
      return;

    case '4':
      print('[BARCO CARGUERO] Ecrible el número de productos que desea añadir:');
      input = stdin.readLineSync();
      int value = int.tryParse(input);

      CargoShip cargoShip = CargoShip();
      cargoShip.call([value]);
      return;
  }

}
