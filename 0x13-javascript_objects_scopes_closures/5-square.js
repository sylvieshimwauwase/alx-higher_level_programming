#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
