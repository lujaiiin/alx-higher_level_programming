#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i;
  const x = Number(process.argv[2]);
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
