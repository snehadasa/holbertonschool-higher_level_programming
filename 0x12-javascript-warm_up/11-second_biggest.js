#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  arr.sort(function (a, b) { return (b - a); });
  console.log(arr[1]);
}
