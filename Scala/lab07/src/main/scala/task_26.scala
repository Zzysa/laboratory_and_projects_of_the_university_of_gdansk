def indices[A](l: List[A], el: A): Set[Int] = {
    l.zipWithIndex.foldLeft(Set())((acc, element) => if (element._1 == el) (acc + element._2) else acc)
}

@main
def task_26: Unit = {
    val lista = List(1, 2, 1, 1, 5)
    println(indices(lista, 1)) // ==> Set(0, 2, 3).
    println(indices(lista, 7)) // ==> Set()
}
