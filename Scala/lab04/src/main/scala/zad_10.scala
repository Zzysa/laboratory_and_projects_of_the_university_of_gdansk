def sum(l: List[Elem]): Elem = {
    @annotation.tailrec 
    def helper(list: List[Elem], acc: Elem = None): Elem = list match {
      case Some(some) :: other if some > 0 => 

        val newAcc = acc match {
          case Some(number) => Some(number + some)
          case None => Some(some) 
        }
        helper(other, newAcc)

      case _ :: other => helper(other, acc)
      case _ => acc
    }
      
    helper(l)
}

type Elem = Option[Double]

@main 
def task_10: Unit = {
  val l = List(Some(2.5), None, None, Some(1.5), Some(-1.5))
  println(sum(l))
}

