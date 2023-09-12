#!/usr/bin/node
exports.incrementAndCall = function (number, theFunction) {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};
