#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let i;
  const x = Number(process.argv[2]);
  for (i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
