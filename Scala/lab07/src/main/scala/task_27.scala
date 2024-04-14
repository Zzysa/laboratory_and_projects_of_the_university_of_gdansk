def swap[A](l: List[A]): List[A] = {
    l.zipWithIndex
    .foldLeft(List(): List[A])((acc, elem) =>   
        if (l.length - 1 != elem._2 || l.length % 2 == 0) {
            if (elem._2 % 2 == 0) acc :+ elem._1 :+ elem._1
            else acc.updated(acc.length - 2, elem._1)
        } else {
            acc :+ elem._1
        })
}   

@main 
def task_27: Unit = {
    val lista = List(1, 2, 3, 4, 5)
    println(swap(lista))
    val lista2 = List(1, 2, 3, 4)
    println(swap(lista2))
    val lista3 = List()
    println(swap(lista3))
}