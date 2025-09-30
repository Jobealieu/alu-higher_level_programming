#!/usr/bin/node
const fs = require('fs');

// Get file paths from command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Read contents of fileA and fileB
const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');

// Write concatenated content into fileC
fs.writeFileSync(fileC, contentA + contentB);
