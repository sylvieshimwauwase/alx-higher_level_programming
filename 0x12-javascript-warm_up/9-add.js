#!/usr/bin/node

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

function add (arg1, arg2) {
  return (arg1 + arg2);
}

console.log(add(arg1, arg2));
