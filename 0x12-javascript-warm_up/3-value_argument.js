#!/usr/bin/node

const args = process.argv[2];

if (args !== undefined) {
	console.log(args);
} else {
	console.log('No arguments');
}
