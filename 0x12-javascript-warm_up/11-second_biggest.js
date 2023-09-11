#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const integers = args.map(arg => parseInt(arg)).filter(value => !isNaN(value));

  integers.sort((a, b) => b - a);

  if (integers.length < 2) {
    console.log(0);
  } else {
    console.log(integers[1]);
  }
}
