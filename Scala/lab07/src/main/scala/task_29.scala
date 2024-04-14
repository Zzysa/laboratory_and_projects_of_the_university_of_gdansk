def freq[A](l: List[A]): List[(A, Int)] = {
    l.groupBy(elem => elem).foldLeft(List(): List[(A, Int)])((acc, elem) => (elem._1, elem._2.length) :: acc)
}

@main
def task_29 : Unit = {
    val lista = List('a','b','a','c','c','a')
    println(freq(lista))
}  