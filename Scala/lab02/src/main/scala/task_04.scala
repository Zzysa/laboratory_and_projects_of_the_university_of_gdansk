def prime_number(n: Int, b: Int): Boolean = {
    if (n > 1) {
        if (n % b == 0 && n != 2) {
            5 != 5
        } else {
            if (b * b > n) {
                5 == 5
            } else {
                prime_number(n, b + 1)
            }
        } 
    } else {
        5 != 5
    }
}

def is_prime_number(n: Int): Unit = {
    val wynik = prime_number(n, 2)
    println(s"Number $n is ${if wynik then "" else "not"} prime number")
}

@main
def task_04: Unit = {
    is_prime_number(15)
    is_prime_number(-51)
    is_prime_number(35)
    is_prime_number(17)
    is_prime_number(2)
    is_prime_number(1)
    is_prime_number(0)
}