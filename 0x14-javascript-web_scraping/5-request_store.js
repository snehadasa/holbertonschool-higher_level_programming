#!/usr/bin/node

const request = require('request');
const fs = require('fs');
request.get(process.argv[2], function (err, response, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, 'utf-8', function (err, data) {
    if (err) throw err;
  });
});
