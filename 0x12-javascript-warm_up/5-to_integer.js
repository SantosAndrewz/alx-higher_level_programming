#!/usr/bin/node
// script prints my number

const convArg = parseInt(process.argv[2]);

if (isNaN(convArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convArg);
}
