import io.Source

def histogram(max: Int): Unit = {
        val text = Source.fromFile("ogniem_i_mieczem.txt").toList

        val sortLettersWithAmount = text
        .filter((el) => el.isLetter == true)
        .map((el) => el.toLower)
        .map((char) => (char, text.filter((el) => el == char).length))
        .toSet
        .toList
        .sortBy(_._2)
        .reverse

        sortLettersWithAmount
        .foreach((el) => println(s"${el._1}:${"*" * ((el._2 * max) / sortLettersWithAmount(0)._2).toInt}"))  
}

@main
def task_34: Unit = {
   println(histogram(30))
}