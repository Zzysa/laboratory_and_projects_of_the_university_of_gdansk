def clearWithCount[A](list: List[A]): List[(A, Int)] = {
  @annotation.tailrec
  def helper(l: List[A], result: List[(A, Int)] = Nil, acc: Int = 1): List[(A, Int)] = l match {
      case Nil => Nil
      case a1 :: a2 :: tail => 
        if a1 == a2 
          then helper(a2 :: tail, result, acc + 1)
        else helper(a2 :: tail, (a1, acc) :: result, 1)
      case a :: Nil => ((a, acc) :: result).reverse
  }

  helper(list)
}

@main
def task_16: Unit = {
  val lista = List(1, 1, 2, 4, 4, 4, 1, 3)
  println(clearWithCount(lista))
  val lista2 = List()
  println(clearWithCount(lista2))
  val lista3 = List(1,1,2,2,3,3,3,3,3,3,1,1,1,2,5,7,8,5,8)
  println(clearWithCount(lista3))
}

