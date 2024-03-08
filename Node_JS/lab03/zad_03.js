function toArray(object1, object2) {
    let objects = [object1, object2]
    let newArray = []

    for (let k = 0; k < 2; k++) {
        if (objects[k] instanceof Array) {
            for(let j = 0; j < objects[k].length; j++) {
                newArray.push(objects[k][j])
            }
        } else {
            newArray.push(objects[k])
        }

    }
        
    return newArray
}

console.log(toArray(1, 2))
console.log(toArray(1, "tekst")) 
console.log(toArray("aa", [1, 2])) 
console.log(toArray([1], null))


// toArray(1, 2) => [1, 2]
// toArray(1, "tekst") => [1, "tekst"]
// toArray("aa", [1, 2]) => ["aa", 1, 2]
// toArray([1], null) => [1, null]
