def remElems[A](list: List[(A)], k: Int): List[(A)] = {
    list.zipWithIndex.map((element) => if (element._2 == k) null else element).filter(_ != null).map((element) => element._1)
}

@main
def task_22: Unit = {
    val l = List('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    println(remElems(l, 4))
    println(remElems(l, -3))
    println(remElems(l, 15))
    println(remElems(l, 1))
    println(remElems(l, 3))
}