#!/usr/bin/node

const array = require('./100-data.js').list;
console.log(array);
const map1 = array.map((index, ele) => index * ele);
console.log(map1);
