function counter(number, miliseconds) {
    return (() => {
        let counter = 2
        ID = setInterval(() => {
            console.log(counter)
            counter++
            if (counter === number) {
                clearInterval(ID)
            }
        }, miliseconds)
    })()
}

counter(5, 1000)