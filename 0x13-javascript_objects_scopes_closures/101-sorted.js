#!/usr/bin/node

const data = require('./101-data');
const myDict = data.dict;

const newDict = {};
for (const key in myDict) {
  const value = myDict[key];

  if (newDict[value]) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}
console.log(newDict);
