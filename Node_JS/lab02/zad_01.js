numbers = [4, 3, 5, 1, 3, 2, 21, 1, 65, -43, 9]
repeat_numbers = []
number_amount = 0
unique_numbers = []

console.log(`\nOur array is ${numbers}\n`)

for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
        if (numbers[j] === numbers[i]) {
            number_amount += 1
        }
    }
        
    if (number_amount === 1) {
        unique_numbers.push(numbers[i])
    }

    if (number_amount == 1) {
        console.log('Number', numbers[i], 'repeats', number_amount, 'time')
    } else {
        console.log('Number', numbers[i], 'repeats', number_amount, 'times')
    }
    
    number_amount = 0
}

console.log(`\nArray of unique numbers is ${unique_numbers}\n`)

