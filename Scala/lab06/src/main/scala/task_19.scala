def subseq[A](list: List[A], begIdx: Int, endIdx: Int): List[A] = {
  list.take(endIdx + 1).drop(if (begIdx < 0) then 0 else begIdx)
}

@main
def task_19: Unit = {
  val list = List(1,2,3,4,5,6)
  println(subseq(list, 2, 4))
  println(subseq(list, -2, 4))
  println(subseq(list, 2, -4))
  println(subseq(list, -2, -4))
}

