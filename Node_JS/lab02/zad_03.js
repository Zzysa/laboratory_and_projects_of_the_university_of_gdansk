const testArray = [1, 2, null, [4, undefined, 11, 10], 6, [7, null, 0], null, 9]; 
newArray = []

for (let i = 0; i < testArray.length; i++) {
    if (testArray[i] !== null && testArray[i] !== undefined && typeof testArray[i] === "object") {
        for(let j = 0; j < testArray[i].length; j++) {
            newArray.push(testArray[i][j])
        }
    } else {
        newArray.push(testArray[i])
    }
}

console.log("Origin array is" , testArray)
console.log("New array is" , newArray)
