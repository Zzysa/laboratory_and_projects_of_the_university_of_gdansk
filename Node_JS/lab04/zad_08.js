function getCounter (min, max) {
    if (min > max) {
        console.log(undefined)
        return undefined
    } else {
        console.log(min);
        getCounter(min + 1, max)
    }
}

getCounter(5,7)