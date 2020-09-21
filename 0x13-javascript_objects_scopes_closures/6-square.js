#!/usr/bin/node

const original_square = require('./5-square');

module.exports = class Square extends original_square {
  charPrint(c) {
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        c = 'X';
      }
     console.log(c.repeat(this.height));
     }
   }
};
