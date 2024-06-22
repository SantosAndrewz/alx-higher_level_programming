#!/usr/bin/node
// a script printing x times 'C is fun'

const t = parseInt(process.argv[2]);

if (isNaN(t)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < t; x++) {
    console.log('C is fun');
  }
}
