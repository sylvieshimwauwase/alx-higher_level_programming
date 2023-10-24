#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const characterId ='18';
let n = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach(film) =>
      film.characters.forEach(character) => {
        if (character.includes(characterId)) {
          n += 1;
        }
      });
    });
    console.log(n);
  }
});
