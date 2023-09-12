#!/usr/bin/node

const fs = require('fs');

function concatFiles(sourceFile1, sourceFile2, destinationFile) {
  try {
    const data1 = fs.readFileSync(sourceFile1, 'utf8');
    const data2 = fs.readFileSync(sourceFile2, 'utf8');
    const concatenatedData = data1 + data2;

    fs.writeFileSync(destinationFile, concatenatedData);

    console.log(`Concatenated ${sourceFile1} and ${sourceFile2} to ${destinationFile}`);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.log('Usage: node concat.js <sourceFile1> <sourceFile2> <destinationFile>');

} else {
  concatFiles(sourceFile1, sourceFile2, destinationFile);
}
