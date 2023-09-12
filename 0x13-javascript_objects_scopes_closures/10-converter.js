#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase (number) {
    return number.toString(base);
  };
};
