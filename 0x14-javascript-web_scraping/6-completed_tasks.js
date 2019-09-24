#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (err) throw err;
  const dic = {};
  const b = JSON.parse(body);
  for (let i in b) {
    let t = b[i]
    if (t.completed) {
      if (t.userId in dic) {
        dic[t.userId] += 1;
      } else {
        dic[t.userId] = 1;
      }
    }
  }
  console.log(dic);
});
