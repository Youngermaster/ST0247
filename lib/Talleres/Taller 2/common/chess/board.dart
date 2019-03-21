import 'dart:io';

class Board {

  List<List<int>> board = new List();
  int size;

  Board(this.size, bool zero) {

    board = new List<List<int>>();//new List.generate(zero ? 0 : size, (_) => new List(zero ? 0 : size));

    if(!zero)
      for(int i = 0; i < size; i++) {

        List<int> cache = new List<int>();

        for (int j = 0; j < size; j++)
          cache.add(0);

        board.add(cache);

      }

  }

  void printBoard() {

    for(int i = 0; i < board.length; i++) {
      for (int j = 0; j < board.length; j++)
        stdout.write(board[i][j].toString() + "\t");
      print("");
    }

  }

  int getSize() => size;

  List<List<int>> getBoard() => board;

}