#!/usr/bin/node
exports.callMeXTimes = function (x, theFunction) {
  if (x <= 0) {
    return;
  }

  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
