function sum(n) {
    if (n === 1) {
        return n
    } else {
        return n + sum(n - 1)
    }
}

console.log(sum(6))