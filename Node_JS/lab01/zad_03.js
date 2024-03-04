numbers = [1, -6, 5, -7, 11, 0]
max = numbers[0]
min = numbers[0]
reverse_numbers = []

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i])
} 

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
        max = numbers[i]
    }
}
console.log(`Max element in 'numbers' is ${max}`)


for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] < min) {
        min = numbers[i]
    }
}
console.log(`Max element in 'numbers' is ${min}`)

for(let i = numbers.length - 1; i >= 0; i--) {
    reverse_numbers.push(numbers[i])
}

console.log(`Reverse array of 'numbers' is ${reverse_numbers}`)
console.log(`Original array of 'numbers' is ${numbers}`)

