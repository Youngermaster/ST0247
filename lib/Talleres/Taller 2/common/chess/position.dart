class Position {

  int x, y;

  Position(this.x, this.y);

  int getX() => x;

  int getY() => y;

  Position clone() {
    return new Position(this.x, this.y);
  }

  Position add(int x, int y) {

    this.x += x;
    this.y += y;

    return this;

  }

}