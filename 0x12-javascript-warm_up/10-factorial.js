#!/usr/bin/node

const result = factorial(Number(process.argv[2]));
console.log(result);

function factorial (num) {
  let value = 1;
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    value = num * factorial(num - 1);
    return (value);
  }
}
