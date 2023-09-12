#!/usr/bin/node

const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

const content1 = fs.readFileSync(file1, 'UTF-8');
const content2 = fs.readFileSync(file2, 'UTF-8');
const combinedContent = content1 + content2;
fs.writeFileSync(file3, combinedContent);
