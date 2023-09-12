#!/usr/bin/node

let numOfArgPrinted = -1;
exports.logMe = function (item) {
  numOfArgPrinted++;
  console.log(numOfArgPrinted + ': ' + item);
};
