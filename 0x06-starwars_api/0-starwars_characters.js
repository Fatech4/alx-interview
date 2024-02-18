#!/usr/bin/node

const request = require('request');

const arg = process.argv;

if (arg.length === 3 && !isNaN(arg[2])) {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${parseInt(
    arg[2]
  )}`;

  request(filmUrl, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Failed to fetch film data:', error);
      return;
    }

    const charactersUrls = JSON.parse(body).characters;
    const charactersPromises = charactersUrls.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error || response.statusCode !== 200) {
            reject(
              error ||
                new Error(`Failed to fetch character data from ${characterUrl}`)
            );
            return;
          }
          resolve(JSON.parse(body).name);
        });
      });
    });

    Promise.all(charactersPromises)
      .then((charactersData) => {
        charactersData.forEach((character) => {
          console.log(character);
        });
      })
      .catch((error) => {
        console.error('Error fetching character data:', error);
      });
  });
} else {
  console.log('Input Valid Argument');
}
