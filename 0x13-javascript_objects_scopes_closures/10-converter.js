#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (a) {
    return a.toString(base);
  }
  return myConverter;
};
