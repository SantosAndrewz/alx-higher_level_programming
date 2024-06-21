#!/usr/bin/node
// script prints my number

const conv_arg = parseInt(process.argv[2]);

if (isNaN(conv_arg)) {
	console.log('Not a number');
}
else {
	console.log('My number: ' + conv_arg);
}
