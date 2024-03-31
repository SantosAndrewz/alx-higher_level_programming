#!/usr/bin/node
const num_Args = process.argv.length - 2;

if (num_Args === 0) {
	console.log('No argument');
}
else if (num_Args === 1) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
