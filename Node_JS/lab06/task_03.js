const arr = [ { x: 4, y: 2}, { x: 1, y: 8 }, { x: 4, y: 2 } ];

function averageValue(objects, key) {
    let sum = 0

    for (let i = 0; i < objects.length; i++) {
        sum = sum + objects[i][key]
    }

    let average = sum / objects.length

    return average
} 

console.log(averageValue(arr, 'y'))