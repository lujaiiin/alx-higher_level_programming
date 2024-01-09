#!/usr/bin/node
const dic = require('./101-data').dic;

const tot = Object.entries(dic);
const va = Object.values(dic);
const vaU = [...new Set(va)];
const nDict = {};
for (const j in vaU) {
  const li = [];
  for (const q in tot) {
    if (tot[q][1] === vaU[j]) {
      li.unshift(tot[q][0]);
    }
  }
  nDict[vaU[j]] = li;
}
console.log(nDict);
