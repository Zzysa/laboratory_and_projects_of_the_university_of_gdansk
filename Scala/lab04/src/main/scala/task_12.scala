def usun[A](l: List[A], el: A): List[A] = { 
    @annotation.tailrec 
    def helper(l: List[A], el: A, result: List[A] = Nil): List[A] = l match  {
        case head :: tail => {
            if (el != head) {
                helper(tail, el, result :+ head)
            } else {
                helper(tail, el, result)                
            }
        } 
        case Nil => result
    }

    helper(l, el)
}

@main 
def tast_12: Unit = {
    val lista = List(2, 1, 4, 1, 3, 3, 1, 2)

    println(usun(lista, 1)) 
}
