def freqMax[A](list: List[A]): (Set[A],Int) = {
    list.map((element) => (element, list.count(_ == element))).filter(_._2 == list.map((element) => (list.count(_ == element))).max).
    distinct.foldLeft((Set(), 0))((acc, element) => if (acc._2 == 0) (acc._1 + element._1, element._2) else (acc._1 + element._1, element._2))
}

@main
def task_23: Unit = {
    val l = List(1, 1, 2, 4, 4, 3, 4, 1, 3)
    println(freqMax(l)) 
}