#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let n = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          n += 1;
        }
      });
    });
    console.log(n);
  }
});
