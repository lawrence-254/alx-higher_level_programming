#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const request = require('request');

request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    const users = {};
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (todos[i].userId in users) {
          users[todos[i].userId]++;
        } else {
          users[todos[i].userId] = 1;
        }
      }
    }
    console.log(users);
  }
});
