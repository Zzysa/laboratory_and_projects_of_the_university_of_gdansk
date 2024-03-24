def isOrdered[A](leq: (A, A) => Boolean)(l: List[A]): Boolean = l match {
    case Nil => true
    case _ :: Nil => true
    case first :: second :: tail => leq(first, second) && isOrdered(leq)(second :: tail)
}

@main
def task_17: Unit = {
    val lt = (m: Int, n: Int) => m < n
    val lte = (m: Int, n: Int) => m <= n
    val lista = List(1, 2, 2, 5)
    println(isOrdered(lt)(lista)) // ==> false
    println(isOrdered(lte)(lista)) // ==> true
}
