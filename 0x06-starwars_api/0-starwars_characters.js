#!/usr/bin/node
const request = require('request');

function Request (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, res, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

async function starwars () {
  if (process.argv < 3) return;

  const Url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  const movie = await Request(Url);

  if (movie.characters === undefined) return;
  for (const characterUrl of movie.characters) {
    const character = await Request(characterUrl);
    console.log(character.name);
  }
}

starwars();
