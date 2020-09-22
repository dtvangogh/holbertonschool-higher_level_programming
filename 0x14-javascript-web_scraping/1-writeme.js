#!/usr/bin/node

const fs = require('fs');
const arguments = process.argv;
let fileName = arguments[2];
let string = arguments[3];

fs.writeFile(fileName, string, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});