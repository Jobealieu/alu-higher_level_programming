#!/usr/bin/node
const argv = process.argv;
function factorial (n) {
  const num = Number.parseInt(n, 10);
  if (Number.isNaN(num)) return 1;
  if (num <= 1) return 1;
  return num * factorial(num - 1);
}
console.log(factorial(argv[2]));
