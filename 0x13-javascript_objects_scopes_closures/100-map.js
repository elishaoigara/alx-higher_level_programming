#!/usr/bin/node
const { list } = require('./100-data.js'); // Import the list from the 100-data.js file

// Create a new list where each element is multiplied by its index
const newList = list.map((value, index) => value * index);

// Print both the original and new lists
console.log(list);
console.log(newList);

