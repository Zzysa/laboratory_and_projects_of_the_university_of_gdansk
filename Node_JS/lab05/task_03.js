// Input: 
// [ 1, 3, 6, 2, 9 ]

// Output: 
// [ '0: 1', '1: 3', '2: 6', '3: 2', '4: 9' ]

const indexAndElement = (array) => {return array.map((element, index) => `${index}: ${element}`)}

const numbers = [ 1, 3, 6, 2, 9 ] 
console.log(indexAndElement(numbers))