#!/usr/bin/node
let va = 0;

exports.logMe = function (item) {
  console.log(va + ': ' + item);
  va++;
};
