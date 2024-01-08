#!/usr/bin/node
function factor (num) {
 let i;
 if (num === 0 || num === 1 || isNaN(num)) {
   return 1;
 } else if (num < 0) {
   return -1;
 }
 for (i = num - 1; i >= 1; i--) {
   num = num * i;
 }
 return num;
}
console.log(factor(Number(process.argv[2])));
