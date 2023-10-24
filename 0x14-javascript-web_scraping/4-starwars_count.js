#!/usr/bin/node
// a script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};
let count = 0;

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const movies = JSON.parse(body).results;
  for (const movie of movies) {
    for (const character of movie.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
