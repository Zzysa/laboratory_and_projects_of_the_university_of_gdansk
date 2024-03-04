const array = [ 4, 2, 'a', 'b', 3, 'aa', 'ww', 2, 'ab', -2];
sort_array = []
for (let i = 0; i < array.length; i++) {
    if (typeof array[i] === typeof 1) {
        console.log(array[i], "=>", typeof array[i])
        sort_array.push(array[i])
    }
}

for (let i = 0; i < array.length; i++) {
    if (typeof array[i] === typeof "i") {
        console.log(array[i], "=>", typeof array[i])
        sort_array.push(array[i])
    }
}

console.log(sort_array)