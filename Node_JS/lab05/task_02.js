// [ -5, 4, -2, 4, -5 ] -> [ 25, 4, 4, 4, 25 ]

const numbers = [ -5, 4, -2, 4, -5 ]

const squareNegative = (array) => {return array.map((element) => element < 0 ? element * element : element)}


console.log(squareNegative(numbers))