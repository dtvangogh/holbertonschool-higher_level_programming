#!/usr/bin/node

let request = require('request');
let fs = require('fs');
let createdFile = process.argv[3];
let url = process.argv[2];

request(url, function (err, response, body) {
  if (err) throw err;
  fs.writeFile(createdFile, body, 'utf8', function (err) {
    if (err) throw err;
  });
});