#!/usr/bin/node

let request = require('request');
let dictionary = {};

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  for (let task of JSON.parse(body)) {
    if (task.completed === true) {
      if (dictionary[task.userId] === undefined) {
        dictionary[task.userId] = 0;
      }
      dictionary[task.userId]++;
    }
  }
  console.log(dictionary);
});