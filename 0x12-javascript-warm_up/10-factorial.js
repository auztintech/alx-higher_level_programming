#!/usr/bin/node
const computeFactorial = (n) => {
  if (isNaN(parseInt(n))) {
    return 1;
  } else if (n <= 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
};

const input = parseInt(process.argv[2]);

console.log(computeFactorial(input));
