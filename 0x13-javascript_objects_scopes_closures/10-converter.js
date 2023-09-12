#!/usr/bin/node
exports.converter = function (base) {
  if (this === 0) {
    return '';
  } else {
    const quotient = Math.floor(this / base);
    const remainder = this % base;
    return converter.call(quotient, base) + remainder;
  }
};
