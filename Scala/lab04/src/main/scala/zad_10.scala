def sum(l: List[Elem]): Elem = {
    @annotation.tailrec 
    def helper(lista: List[Elem], acc: Elem = None): Elem = lista match {
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

type Elem = Option[Double]

@main 
def mainProg: Unit = {
  val l = List(Some(2.5), None, None, Some(1.5), Some(-1.5))
  println(sum(l))
}

