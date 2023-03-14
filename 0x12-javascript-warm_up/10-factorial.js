#!/usr/bin/node
function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}

console.log(factorial(Number(process.argv[2])));
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
