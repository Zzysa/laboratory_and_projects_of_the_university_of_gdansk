let counter = 0

function welcome() {
    let ID = setInterval(() => {
        counter++
        console.log("Welcome!") 

        if (counter === 5) {
            clearInterval(ID)
        }
    }, 1000);
}

welcome()