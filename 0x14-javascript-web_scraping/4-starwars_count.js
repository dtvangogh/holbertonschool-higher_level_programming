#!/usr/bin/node

const request = require('request');
let count = 0;

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  const films = JSON.parse(body).results;
  for (const film of films) {
    for (const actor of film.characters) {
      if (actor.endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
