#!/usr/bin/node
const args = process.argv;
add(Number(args[2]), Number(args[3]));

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
