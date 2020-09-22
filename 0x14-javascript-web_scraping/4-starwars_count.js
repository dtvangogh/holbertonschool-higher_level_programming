#!/usr/bin/node

const request = require('request');
let count = 0;

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  let films = JSON.parse(body).results;
  for (let film of films) {
    for (let actor of film.characters) {
      if (actor.endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});