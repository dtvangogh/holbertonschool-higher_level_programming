#!/usr/bin/node

const request = require('request');
request('http://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
  const characters = JSON.parse(body).characters
  if (err) throw err;
  for (let character of characters) {
    request(character, function (err, response, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  }
});