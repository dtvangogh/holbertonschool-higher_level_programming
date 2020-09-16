#!/usr/bin/node

function add (x, y) {
  return x + y;
}

let number1 = parseInt(process.argv[2]);
let number2 = parseInt(process.argv[3]);

console.log(add(number1, number2));
