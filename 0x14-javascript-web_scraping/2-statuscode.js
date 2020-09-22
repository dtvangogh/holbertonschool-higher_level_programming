#!/usr/bin/node

const argument = process.argv;
const url = argument[2];
const request = require('request');

request.get(url).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
