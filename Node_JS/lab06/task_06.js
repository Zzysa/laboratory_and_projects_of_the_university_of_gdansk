const { lp3 } = require('./toplist');
const _ = require('lodash');

let n = process.argv[2];
let min = process.argv[3];
let max = process.argv[4];
let rand = _.random(min + 1, max - 1)

for (let i = 0; i < n; i++) {
    console.log(lp3[rand].song)
}