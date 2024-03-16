def listMax(l1: List[Double], l2: List[Double]): List[Double] =  {
  @annotation.tailrec 
  def helper(l1: List[Double], l2: List[Double], result: List[Double] = Nil) : List[Double] = (l1, l2) match {
    case (some1 :: other1, some2 :: other2) => 
      if (some1 >= some2) {
        helper(other1, other2, result :+ some1)
      } else { 
        helper(other1, other2, result :+ some2)
      }
    case (Nil , some) => result ++ some
    case (some, Nil) => result ++ some
  }

  helper(l1, l2)
}

@main 
def task_11: Unit = {
    val list1 = List(2.0, -1.6, 3.2, 5.4, -8.4)
    val list2 = List(3.3, -3.1, 3.2, -4.1, -0.4, 5.5)
    val list3 = List()
    println(listMax(list1, list2))
    println(listMax(list3, list3))


}