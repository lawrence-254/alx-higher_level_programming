#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');
const options = {
  url: process.argv[2],
  method: 'GET'
};
const filepath = process.argv[3];

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(filepath, body, 'UTF-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
