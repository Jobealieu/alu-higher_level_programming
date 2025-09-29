#!/usr/bin/node
const args = process.argv.slice(2).map((v) => parseInt(v, 10));

if (args.length <= 1) {
  console.log(0);
} else {
  // Find largest and second largest in one pass
  let largest = -Infinity;
  let second = -Infinity;

  for (const n of args) {
    if (n > largest) {
      second = largest;
      largest = n;
    } else if (n > second && n < largest) {
      second = n;
    }
  }

  // If all numbers equal or second stayed -Infinity, print 0 (spec not explicit, examples imply reasonable behavior)
  console.log(second === -Infinity ? 0 : second);
}
