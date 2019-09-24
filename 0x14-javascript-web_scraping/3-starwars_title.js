#!/usr/bin/node

const request = require('request');
request.get('https://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) throw err;
  const starwars = JSON.parse(body).title;
  console.log(starwars);
});
