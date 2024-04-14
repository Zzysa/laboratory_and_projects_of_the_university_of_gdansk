def position[A](l: List[A], el: A): Any = {
    l.zipWithIndex.find(x => x._1 == el).map(_._2)
}


@main
def task_25: Unit = {
    val lista = List(2, 1, 1, 5)
    println(position(lista, 1)) // ==> Some(1)
    println(position(lista, 3)) // ==> None
    println(position(lista, 5)) // ==> None

}
