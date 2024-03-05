def goldbachs_conjecture(n: Int, first: Int, second: Int): String = {
    if (prime_number(first, 2) && prime_number(second, 2) && first + second == n) {
        s"$n = $first + $second"
    } else {
        if (second < first) {
            goldbachs_conjecture(n, first - 1, second + 1)
        } else {
            "We cant find two prime numbers"
        }
        
    }
}

def hypothesis(n: Int): String = {
    if (n % 2 == 0) {
        if (n > 0) {
            goldbachs_conjecture(n, n - 2, 2)
        } else {
            s"Number $n is not a natural number"
        }
    } else {
        s"Number $n is odd number"
    }
}

@main
def task_05: Unit = {
    println(hypothesis(24))
    println(hypothesis(462))
    println(hypothesis(13))
    println(hypothesis(-15))
    println(hypothesis(0))
    println(hypothesis(-16))

}