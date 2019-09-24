#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (err) throw err;
  const starwars = JSON.parse(body).results;
  let c = 0;
  for (let i = 0; i < starwars.length; i++) {
    for (let j = 0; j < starwars[i].characters.length; j++) {
      if (starwars[i].characters[j].includes('/18/')) {
        c++;
      }
    }
  }
  console.log(c);
});
