#!/usr/bin/node

const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = size; i > 0; i--) {
    let square = '';
    for (let j = size; j > 0; j--) {
      square += 'X';
    }
    console.log(square);
  }
}
