#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const createdFile = process.argv[3];
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) throw err;
  fs.writeFile(createdFile, body, 'utf8', function (err) {
    if (err) throw err;
  });
});
