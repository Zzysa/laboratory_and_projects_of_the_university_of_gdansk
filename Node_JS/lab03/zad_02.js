function isPositiveEven(number) {
    if (number % 2 === 0 && number > 0) {
        console.log(`${number} is positive and more then zero`)
    } else {
        console.log(`${number} is not positive and more then zero`)
    }
}

isPositiveEven(-6)
isPositiveEven(16)
isPositiveEven(-5)
isPositiveEven(5)