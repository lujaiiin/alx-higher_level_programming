#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    let x;
    for (i = 0; i < this.height; i++) {
      x = '';
      for (j = 0; j < this.width; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
}

module.exports = Rectangle;
