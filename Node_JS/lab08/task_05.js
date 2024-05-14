function helloWorld() {
    console.log("Hello World!")
}

function loop(callback, miliseconds, end_loop) {
    let seconds = 0

    ID = setInterval(() => {
        callback()
        seconds = seconds + miliseconds
        if (seconds === end_loop) {
            clearInterval(ID)
        }
    }, miliseconds * 1000)
}

loop(helloWorld, 2, 6)



