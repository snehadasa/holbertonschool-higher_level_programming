#!/usr/bin/node

const request = require('request');
request.get('https://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) throw err;
  const starwars = JSON.parse(body);
  for (const i of starwars.characters) {
    request.get(i, function (err, response, body) {
      if (err) throw err;
      const starwars = JSON.parse(body);
      console.log(starwars.name);
    });
  }
});
