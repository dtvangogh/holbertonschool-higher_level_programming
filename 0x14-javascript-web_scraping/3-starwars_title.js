#!/usr/bin/node

const request = require('request');
const filmNumber = process.argv[2];

request('https://swapi-api.hbtn.io/api/films/' + filmNumber, function (err, response, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
