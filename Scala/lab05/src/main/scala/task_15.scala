def clear[A](list: List[A]): List[A] = {
  @annotation.tailrec
  def helper(l: List[A], result: List[A] = Nil): List[A] = l match {
      case Nil => Nil
      case a1 :: a2 :: tail => 
        if a1 == a2 
        then helper(a2 :: tail, result)
        else helper(a2 :: tail, a1 :: result)
      case a :: Nil => (a :: result).reverse
  }

  helper(list)
}

@main
def task_15: Unit = {
  val lista = List(1, 1, 2, 4, 4, 4, 1, 3)
  println(clear(lista))
  val lista2 = List()
  println(clear(lista2))
  val lista3 = List(1,1,2,2,3,3,3,3,3,3,1,1,1,2,5,7,8,5,8)
  println(clear(lista3))
}

