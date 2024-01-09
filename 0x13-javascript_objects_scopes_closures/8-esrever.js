#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length - 1;
  let j = 0;
  for (l; (len - j) > 0; l--) {
    const tmp = list[l];
    list[l] = list[j];
    list[j] = tmp;
    j++;
  }
  return list;
};
