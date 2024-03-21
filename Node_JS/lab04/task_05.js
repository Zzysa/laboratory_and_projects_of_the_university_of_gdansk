function callFunction(func) {
    return func();
}

function helloWorld() {
    return "Hello World!";
}

console.log(callFunction(helloWorld)); 