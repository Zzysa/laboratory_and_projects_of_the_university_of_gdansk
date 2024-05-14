function timerEnd() {
    console.log("End of Timer")
}

function countdown(seconds, callback) {
    ID = setInterval(() => {
        console.log(seconds) 
        seconds--
        if(seconds < 0) {
            clearInterval(ID)
            callback()
        }
    }, 1000)
}

countdown(6, timerEnd)