#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && ypeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
