#!/usr/bin/node

const script = 'C is fun';
let i = 0;
for (i = 0; i < process.argv[2]; i++) {
  console.log(script);
}
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
