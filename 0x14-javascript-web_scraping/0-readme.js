#!/usr/bin/node
// Reads and prints a file

const arguments = process.argv;
let fs = require('fs');
fs.readFile(arguments[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});