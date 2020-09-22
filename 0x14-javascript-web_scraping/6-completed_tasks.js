#!/usr/bin/node

const request = require('request');
const dictionary = {};

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (dictionary[task.userId] === undefined) {
        dictionary[task.userId] = 0;
      }
      dictionary[task.userId]++;
    }
  }
  console.log(dictionary);
});
