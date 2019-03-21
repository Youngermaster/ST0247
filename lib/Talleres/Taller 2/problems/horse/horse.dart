import '../../common/chess/board.dart';
import '../../common/chess/position.dart';
import '../../problem.dart';

class Horse implements Problem {

  @override
  bool available() => true;

  @override
  void call(args) {

    generate(args[0], true);
    return;

  }

  Board generate(int n, bool show) {
    Board board = new Board(n, false);
    fillPositions(board, n);

    var before = new DateTime.now().millisecondsSinceEpoch;
    start(board, 0, 0, show);
    print('Time: ' + (new DateTime.now().millisecondsSinceEpoch - before).toString() + " ms");
    return board;
  }

  void fillPositions(Board board, int n) {

    print(board.getBoard().length);

    for(int i = 0; i < n; i++)
      board.getBoard()[i][i] = 0;

  }

  bool start(Board board, int moveX, int moveY, bool show) {

    board.getBoard()[moveX][moveY] = 1;
    List<Position> moves = getMoves(board, new Position(moveX, moveY));

    if(moves.isEmpty) {

      board.printBoard();
      return true;

    }

    Position next = getGoodPosition(board, moves);

    moveX = next.getX();
    moveY = next.getY();

    if(show) {
      board.printBoard();
      print('\n \n');
    }

    return start(board, moveX, moveY, show);

  }

  List<Position> getMoves(Board board, Position current) {

    var horseMoves = [[2, 1],
                      [2, -1],
                      [-2, 1],
                      [-2, -1],
                      [1, 2],
                      [1, -2],
                      [-1, 2],
                      [-1, -2]];

    List<Position> result = new List();

    for(var i in horseMoves)
      if(isValid(board, current.clone().add(i[0], i[1]), board.getSize()))
        result.add(current.clone().add(i[0], i[1]));

    return result;

  }

  Position getGoodPosition(Board board, List<Position> positions) {

    int maximium = 1000;
    Position query = null;

    for(Position position in positions) {

      List<Position> moves = getMoves(board, position);

      if(moves.length < maximium){

        if(moves.length == 7) {

          query = position.clone();
          break;

        }

        query = position.clone();
        maximium = moves.length;

      }

    }

    return query;

  }

  bool isValid(Board board, Position position, int n) {

    if(position.getX() >= n || position.getY() >= n
       || position.getX() < 0 || position.getY() < 0
       || board.getBoard()[position.getX()][position.getY()] == 1)
      return false;

    return true;

  }

  List<int> cloneColumn(List<int> column) {

    List<int> result = new List(column.length);

    for(int i = 0; i < column.length; i++)
      result[i] = column[i];

    return result;

  }

}