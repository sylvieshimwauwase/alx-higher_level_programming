#!/usr/bin/node
const { dict } = require('./101-data');

const invertedDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (!invertedDict[occurrences]) {
    invertedDict[occurrences] = [];
  }
  invertedDict[occurrences].push(userId);
}

console.log(invertedDict);
