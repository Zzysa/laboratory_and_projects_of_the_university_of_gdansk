def count_even(n: Int): Boolean = {
  n % 2 == 0
}

def is_even(n: Int): Unit = {
    val result = count_even(n)
    println(s"Number $n is ${if result then "" else "not"} even")
}

@main
def task_02: Unit = {
  is_even(15)
  is_even(16)
  is_even(1)
  is_even(-18)
}
