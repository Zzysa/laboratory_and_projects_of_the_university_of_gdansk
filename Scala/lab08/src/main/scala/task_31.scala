@main 
def task_31: Unit = {
    val ocenyCzastkowe: List[(String, String, Int, Int)] = List(
    ("Jan", "Kowalski", 16, 12),
    ("Anna", "Nowak", 19, 20),
    ("Jan", "Kowalski", 16, 14),
    ("Anna", "Nowak", 16, 19),
    ("Piotr", "Zieliński", 20, 20),
    ("Ivan", "Test", 17, 12),
    ("Ivan", "Test", 17, 12),
    ("Inna", "Newak", 19, 20),
    ("Inna", "Newak", 16, 19)
    )

    val result = (ocenyCzastkowe
    .groupMap((person) => (person._1, person._2))((marks) => (marks._3, marks._4))
    .map((el) => (el(0), el(1).foldLeft(0.0 , 0.0)((acc, curr) => (curr(0).toDouble / el(1).length + acc(0), curr(1).toDouble / el(1).length + acc(1)))))
    .map((el) => (el(0)(0), el(0)(1), el(1)(0), el(1)(1)))
    .toSeq
    .sortWith((el1, el2) => if (el1._3 + el1._3 > el2._3 + el2._3) el1._3 + el1._3 > el2._3 + el2._3 else el1._3 > el2._3)
    .zipWithIndex
    .map((el) => (el(1) + 1, el(0)._1, el(0)._2, el(0)._3 + el(0)._4))
    )

    println(result)
}

