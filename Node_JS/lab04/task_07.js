function isPalidrom(arr) {
    if (arr.length % 2 == 0) {
        for (let i = 0; i < arr.length / 2; i++) {
            if (arr[i] !== arr[arr.length - 1 - i]) {
                return false
            }
        }
        return true
    } else {
        for (let i = 0; i < arr.length / 2  - 1; i++) {
            if (arr[i] !== arr[arr.length - 1 - i]) {
                return false
            }
        } 
        return true
    }
}

const array = [1,2,3,3,2,1]
console.log(isPalidrom(array))

const array2 = [1,2,3,2,1]
console.log(isPalidrom(array2))

const array3 = [1,2,3,1,1]
console.log(isPalidrom(array3))

const array4 = [1,2,3,2,2,1]
console.log(isPalidrom(array4))