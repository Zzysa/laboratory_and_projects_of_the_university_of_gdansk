case class Ocena(czarne: Int, białe: Int) {
  override def toString = s"czarne: $czarne, białe: $białe"
}

def ocena(kod: List[Int], ruch: List[Int]): Ocena = {
  val czarne = ruch.zip(kod).filter((e) => e._1 == e._2)
  val białe = kod.intersect(ruch).diff(czarne.map((e) => e._1)).length
  Ocena(czarne.length, białe)
}

@main
def task_30: Unit = {
  val secret = List(1, 3, 2, 2, 4, 5)
  val guess = List(2, 1, 2, 4, 7, 2)
  println(ocena(secret, guess))
}

