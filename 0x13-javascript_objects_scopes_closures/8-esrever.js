#!/usr/bin/node
exports.esrever = function (list) {
  let listLen = list.length - 1;
  let i = 0;
  while ((listLen - i) > 0) {
    const temp = list[listLen];
    list[listLen] = list[i];
    list[i] = temp;
    i++;
    listLen--;
  }
  return list;
};
