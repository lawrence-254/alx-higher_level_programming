#!/usr/bin/node
const args = process.argv;
const a = args[2];
const b = args[3];

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
