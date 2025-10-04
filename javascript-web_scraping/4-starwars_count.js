#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    // Loop through all films
    for (const film of data.results) {
      // Check if Wedge Antilles (character ID 18) is in the film's characters list
      for (const character of film.characters) {
        if (character.includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
