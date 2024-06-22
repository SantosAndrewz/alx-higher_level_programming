#!/usr/bin/node
// a script computing and printing a factorial

function factorial (x) {
  if (isNaN(x) || x == 0) {
    return 1;
  } else {
    return x * factorial(x - 1)
  }
}
console.log(factorial(parseInt(process.argv[2])));
