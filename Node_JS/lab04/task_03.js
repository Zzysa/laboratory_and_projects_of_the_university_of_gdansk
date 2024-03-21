function counter() {
    const number1 = 5;
    return function(number2) {
      return number1 + number2
    }
}

var sum = counter();
console.log(sum(5));
console.log(sum(0));
console.log(sum(-5));
