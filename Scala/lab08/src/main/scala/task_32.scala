def threeNumbers(n: Int): List[(Int, Int, Int)] = {
    for {
        a <- (1 to n).toList
        b <- (a + 1 to n).toList
        c <- (b + 1 to n).toList
        if a*a + b*b == c*c
    } yield (a, b, c)
}


@main 
def task_32: Unit = {
   println(threeNumbers(15))
}