#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;

  // Function to print characters in order
  const printCharacter = (index) => {
    if (index >= characters.length) return;
    request(characters[index], (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(body).name);
      printCharacter(index + 1);
    });
  };

  printCharacter(0);
});
