#!/usr/bin/node
// a script printing a square.

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    console.log('X'.repeat(size));
  }
}
