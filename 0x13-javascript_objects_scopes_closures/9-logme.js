#!/usr/bin/node

let val = 0;
exports.logMe = function (item) {
  console.log(val + ': ' + item);
  val++;
};
