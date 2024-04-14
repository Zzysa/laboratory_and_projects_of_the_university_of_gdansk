def sumOpts(l: List[Option[Double]]): Option[Double] = {
  l.foldLeft(None: Option[Double])((acc, number) => (acc, number) match {
    case (None, opt) => opt
    case (Some(num1), Some(num2)) => Some(num1 + num2)
    case (Some(num), None) => Some(num)
  })
}

@main
def task_24: Unit = {
  val lista = List(Some(5.4), Some(-2.0), Some(1.0), None, Some(2.6))
  println(sumOpts(lista) == Some(7.0))
  sumOpts(List()) == None
  sumOpts(List(None, None)) == None
}

