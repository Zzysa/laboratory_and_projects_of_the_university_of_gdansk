def divide[A](l: List[A]): (List[A], List[A]) = {
    @annotation.tailrec 
    def helper(l: List[A], index: Int = 0, l1: List[A] = Nil, l2: List[A] = Nil): (List[A], List[A]) = l match  {
        case head :: tail => {
            if (index % 2 == 0) {
                helper(tail, index + 1, l1 :+ head, l2)
            } else {
                helper(tail, index + 1, l1, l2 :+ head)
            }
        } 
        case Nil => (l1, l2)
    }

    helper(l)
}

@main 
def tast_13: Unit = {
    val lista = List(1, 3, 5, 6, 7)

    println(divide(lista))
}
