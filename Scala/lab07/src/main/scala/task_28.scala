@main
def task_28 : Unit = {
    val strefy: List[String] = java.util.TimeZone.getAvailableIDs.toList
    println(strefy.filter((elem) => elem.startsWith("Europe")).map((elem) => elem.stripPrefix("Europe/")).sortWith(_.length < _.length))
}  
  