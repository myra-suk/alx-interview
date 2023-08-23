#!/usr/bin/node

/*
 * Writes a Script that prints all characters of a Star Wars movie:
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const filmData = JSON.parse(body);
  for (const characterUrl of filmData.characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.log(error);
          return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        resolve();
      });
    });
  }
});
