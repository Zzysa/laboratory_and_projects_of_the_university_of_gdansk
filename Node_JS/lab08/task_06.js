function helloWorld() {
    console.log("Hello World!")
}

function executeAfterDelay(milisekunds, callback) {
    setTimeout(callback, milisekunds)
}

executeAfterDelay(2000, helloWorld)
