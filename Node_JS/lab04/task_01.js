const arr = [10, 'a', 21, true, null, undefined, 1, false, 'b', 2];

const isNull = (element) => element === null

console.log(arr.some(isNull))

const isStringInArr = arr.find((element) => typeof element === 'string')

console.log(isStringInArr);

const isTrue = (element) => element === true;

console.log(arr.findIndex(isTrue));

const numbers = arr.filter((element) => typeof element === 'number')

console.log(numbers.sort((a, b) => a - b))
