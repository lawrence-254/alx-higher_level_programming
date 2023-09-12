#!/usr/bin/node

const data = require('./100-data');
const oldList = data.list;

const newList = oldList.map((value, index) => value * index);

console.log(oldList);
console.log(newList);
