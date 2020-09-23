#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
    if (!error) {
	let characters = JSON.parse(body).characters;
	printInOrder(characters, 0);
    }
});

function printInOrder (characters, index) {
    request(characters[index], function (error, response, body) {
	if (!error) {
	    console.log(JSON.parse(body).name);
	    if (index + 1 < characters.length) {
		printInOrder(characters, index + 1);
	    }
	}
    });
}