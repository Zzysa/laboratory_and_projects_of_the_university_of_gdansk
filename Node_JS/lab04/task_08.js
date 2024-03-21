function getCounter(min, max) {
    let count = min;
    return function() {
        if (count <= max) {
            return count++;
        } else {
            return undefined;
        }
    }
}

const counter = getCounter(5,7);

console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());

const counter2 = getCounter(5,9);

console.log(counter2());
console.log(counter2());

const counter3 = getCounter(5,9);

console.log(counter2());
console.log(counter3());
console.log(counter3());
console.log(counter2());



