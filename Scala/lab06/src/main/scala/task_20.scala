def pairPosNeg(list: List[Double]): (List[Double], List[Double]) = {
    list.filter( _ != 0.0 ).partition( _ < 0)
}

@main
def task_20: Unit = {
  val list = List(1.0 , 2.5, -3.6, 0.0, 7.9, 5.4, -6.9, 0.0)
  println(pairPosNeg(list))
}

