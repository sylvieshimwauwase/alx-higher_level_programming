#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];

fs.readfile(filename, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
