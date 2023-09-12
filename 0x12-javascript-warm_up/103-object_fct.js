#!/usr/bin/node
function incr (number) {
  return number + 1;
}

function callMeXTimes (x, theFunction) {
  if (x <= 0) {
    return;
  }

  for (let i = 0; i < x; i++) {
    theFunction(i);
  }
}

function myFunction (number) {
  console.log(`Incremented number is: ${number}`);
}

const initialNumber = 5;

callMeXTimes(5, (i) => {
  const incrementedNumber = incr(initialNumber);
  myFunction(incrementedNumber);
});
