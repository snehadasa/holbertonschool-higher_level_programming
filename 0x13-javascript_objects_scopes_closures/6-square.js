#!/usr/bin/node

const SquareN = require('./5-square.js');
module.exports = class Square extends SquareN {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
