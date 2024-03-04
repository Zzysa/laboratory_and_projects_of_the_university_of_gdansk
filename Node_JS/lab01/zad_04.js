const numbers = [40, 100, 63];
numbers.sort(function(a, b){return a - b})
is_triangle = true

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] < 0) {
        console.log(`Number ${numbers[i]} is negative and because of that we can't build a triangle`)
        is_triangle = false
        break
    }
}

if (is_triangle) {
    if (numbers[0] + numbers[1] > numbers[2]) {
        console.log(`We can build a triangle with sides ${numbers}`)
    } else {
        console.log(`We can't build a triangle with sides ${numbers}`)
    }
}
