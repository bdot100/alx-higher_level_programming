#!/usr/bin/node

const dict = require('./101-data').dict;
const dictKeys = Object.keys(dict);
const values = Object.values(dict);
let matched;
const resultDict = {};
// loop over the values
for (let i = 0; i < values.length; i++) {
  resultDict[JSON.stringify(values[i])] = [];
  matched = dictKeys.filter(key => dict[key] === values[i]);
  matched.forEach(item => resultDict[JSON.stringify(values[i])].push(item));
}
console.log(resultDict);
