def likeFibonacciNumber(n: Int): Int = {
    @annotation.tailrec
    def likeFibonacci(number: Int, n1: Int, n2: Int): Int = {
        if (number > 1) {
            likeFibonacci(number - 1, n2, n2 + n1)
        } else if (number == 0) {
            2
        } 
        else {
            n2
        }
    }

    likeFibonacci(n, 2, 1)
} 
    

@main
def task_08: Unit = {
    println(likeFibonacciNumber(9))
    println(likeFibonacciNumber(8))
    println(likeFibonacciNumber(7))
    println(likeFibonacciNumber(6))
    println(likeFibonacciNumber(5))
    println(likeFibonacciNumber(4))
    println(likeFibonacciNumber(3))
    println(likeFibonacciNumber(2))
    println(likeFibonacciNumber(1))
    println(likeFibonacciNumber(0))
}