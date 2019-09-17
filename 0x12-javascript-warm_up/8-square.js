#!/usr/bin/node

let i = 0;
for (i = 0; i < process.argv[2]; i++) {
  console.log('X'.repeat(process.argv[2]));
}
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
