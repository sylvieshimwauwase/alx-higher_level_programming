#!/usr/bin/node
exports.converter = function (base) {
  if (this === 0) return '';

  return this >= base
  ? converter.call(Math.floor(this / base), base) + (this % base)
  : String(this);
};
