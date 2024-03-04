numbers = [1, 5, 6, 5, 5, 1, 5]
repeat_numbers = []
number_amount = 0

console.log(`\nOur array is ${numbers}\n`)

for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
        if (numbers[j] === numbers[i]) {
            number_amount += 1
        }
    }

    if (number_amount == 1) {
        console.log('Number', numbers[i], 'repeats', number_amount, 'time')
    } else {
        console.log('Number', numbers[i], 'repeats', number_amount, 'times')
    }
    
    number_amount = 0
}