#!/usr/bin/node

function second_biggest (x) {
  return x.sort().reverse()[1];
}
if (process.argv.length < 4) {
  console.log('0');
} else {
  console.log(second_biggest(process.argv.slice(2)));
}
