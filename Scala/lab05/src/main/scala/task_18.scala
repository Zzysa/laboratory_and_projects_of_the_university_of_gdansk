def applyForAll[A, B](f: A => B)(l: List[A]): List[B] = {
    def helper(f: A => B)(l: List[A], result: List[B] = Nil): List[B] = l match {
        case Nil => result.reverse
        case head :: tail => helper(f)(tail, f(head) :: result)
    } 

    helper(f)(l)
}

@main
def task_18: Unit = {
    val list = List(1, 3, 5)
    val f = (n: Int) => n + 3
    println(applyForAll(f)(list)) // ==> List(4, 6, 8)
}
