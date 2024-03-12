function isAnyEven(array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0){
            return true
        }
    }
    return false
}

console.log(isAnyEven([1, 4, 5, 3]))
console.log(isAnyEven([1, 3, 5, 3]))