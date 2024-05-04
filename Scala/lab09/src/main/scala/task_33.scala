@main
def task_33: Unit = {
  import io.Source
  val osoby = Source.fromFile("nazwiska.txt").getLines.toList
  println(
    osoby
      .map((el) => el.split(" ").toList)
      .map((el) => (el(0).toLowerCase.distinct.length, el(0), el(1).length, el(1)))
      .sortBy(_._1)
      .reverse
      .filter((el) =>
        el._1 == osoby
          .map((el) => el.split(" ").toList)
          .map((el) => (el(0).toLowerCase.distinct.length))
          .sorted
          .reverse(0)
      )
      .sortBy(_._3)
      .reverse
      .map((el) => (el._2, el._4))(0)
  )
}
