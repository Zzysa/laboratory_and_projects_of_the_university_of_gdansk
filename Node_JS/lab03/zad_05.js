function numberSplit(n) {
    if (n % 2 === 0) {
        return [n/2, n/2]
    } else {
        return [(n-1)/2, (n+1)/2]
    }
}

console.log(numberSplit(-15))
console.log(numberSplit(-16))
console.log(numberSplit(-11))
console.log(numberSplit(1))