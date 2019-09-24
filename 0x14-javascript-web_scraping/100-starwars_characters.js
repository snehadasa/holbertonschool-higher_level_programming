#!/usr/bin/node

const request = require('request');
request.get('https://swapi.co/api/people/', function (err, response, body) {
  if (err) throw err;
  const starwars = JSON.parse(body).results;
  for (const i in starwars) {
    for (const j in starwars[i].films) {
      if (starwars[i].films[j].includes(process.argv[2])) {
        console.log(starwars[i].name);
      }
    }
  }
});
