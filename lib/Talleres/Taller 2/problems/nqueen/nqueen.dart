import '../../common/chess/board.dart';
import '../../common/chess/position.dart';
import '../../problem.dart';

class NQueen implements Problem {

  @override
  bool available() =>true;
  
  @override
  void call(args) {

    Board board = args[0] == true ? generateWith3Queens(args[1], args[2]) : generate(args[1]);

    print('El numero de ubicaciones posibles para ' + args[0].toString() + ' reinas es ' + board.getBoard().length.toString());

    for(int i = 0; i < board.getBoard().length; i++)
      print('Ubicación #' + i.toString() + ": " + board.getBoard()[i].toString());

    return;

  }

  Board generateWith3Queens(int n, List<List<int>> queens) {

    Board board = new Board(n, true);

    for(int i = 0; i < 3; i++) {

      List<int> column = new List(n);
      column[queens[i][0]] = queens[i][1];

      board.getBoard().add(cloneColumn(column));

    }

    getPositions(board, new List(n), 0);
    return board;

  }

  Board generate(int n) {
    Board board = new Board(n, true);
    getPositions(board, new List(n), 0);
    return board;
  }

  void getPositions(Board board, List<int> column, int position) {

    if(position == column.length) {
      board.getBoard().add(cloneColumn(column));
      return;
    }

    for(int i = 0; i < column.length; i++) {
      column[position] = i;
      if(!isValid(column, position)) {
        continue;
      }
      getPositions(board, column, position + 1);
    }

  }

  bool isValid(column, int position) {

    for (int i = 0; i <= position; i++) {
      for (int j = i + 1; j <= position; j++) {
        if (column[i] == column[j])
          return false;
        if ((i - j).abs() == (column[i] - column[j]).abs())
          return false;
      }
    }

    return true;
  }

  List<int> cloneColumn(List<int> column) {

    List<int> result = new List(column.length);

    for(int i = 0; i < column.length; i++)
      result[i] = column[i];

    return result;

  }

}