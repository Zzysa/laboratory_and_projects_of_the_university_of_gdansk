def deStutter[A](list: List[A]): List[A] = {
    list.foldLeft(List[A]())((acc, element) => if (acc == Nil || acc.head != element) then element :: acc else acc).reverse
}

@main
def task_21: Unit = {
    val l = List(1, 1, 2, 4, 4, 4, 1, 3)
    println(deStutter(l))
}