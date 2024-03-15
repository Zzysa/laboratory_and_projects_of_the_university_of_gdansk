def reverse(str: String): String = {
  def helper(str:String, result: String): String = {
    if str == "" then result
    else helper(str.tail, s"${str.head}$result")
  }

  helper(str, "")
}
  
@main
def task_06: Unit = {
  println(reverse("Hello world!"))
}

