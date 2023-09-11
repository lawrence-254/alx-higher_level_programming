#!/usr/bin/node
const [, , ...args] = process.argv;

if (args.length < 2) {
  console.log(0);
} else {
  const num = args.sort((a, b) => b - a);

  console.log(num[1]);
}
