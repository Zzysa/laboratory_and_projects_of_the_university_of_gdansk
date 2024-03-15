def max(l1: List[Double], l2: List[Double]): List[Double] = {
    @annotation.tailrec 
    def helper(l1, l2): Elem = lista match {
      case Some(some) :: reszta if some > 0 => 

        val newAcc = acc match {
          case Some(number) => Some(number + some)
          case None => Some(some) 
        }
        helper(reszta, newAcc)

      case _ :: reszta => helper(reszta, acc)
      case _ => acc
    }
      
    helper(l)
}

@main 
def mainProg: Unit = {
    val list1 = List(2.5, 6.0, 15.0, 8.5)
    val list2 = List(4.0, -3.0, 7.0, 5.4)

    println(max(list1, list2))
}