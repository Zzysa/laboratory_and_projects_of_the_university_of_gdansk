const strings = [ 'Ala', 'Janusz', 'kot', 'pies'] // -> Janusz
const numbers = [ 1, 112, 13, 18 ] // -> 112

function biggest(arr) {
    return arr.reduce((acc, current) => {if (typeof current === 'number') {
        return current > acc ? current : acc 
    } else {
        return current.length > acc.length ? current : acc
    }})
}

console.log(biggest(strings))
console.log(biggest(numbers))