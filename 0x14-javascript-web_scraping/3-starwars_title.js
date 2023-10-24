#!/usr/bin/node
// a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');

const argmnt = {
  url: `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  method: 'GET'
};

request(argmnt, function (err, resp, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
