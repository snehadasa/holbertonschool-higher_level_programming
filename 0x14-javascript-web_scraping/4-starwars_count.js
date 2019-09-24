#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (err) throw err;
  const starwars = JSON.parse(body).results.filter(count => {
    const num = count.characters.includes('https://swapi.co/api/people/18/');
    if (num) {
      return (num);
    }
  });
  const c = starwars.length;
  console.log(c);
});
