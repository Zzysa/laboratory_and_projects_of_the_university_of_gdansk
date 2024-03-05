def printGcd(a: Int, b: Int): Unit = {
  println(s"nwd($a,$b) == ${gcd(a, b)}")
}

@annotation.tailrec
def gcd(a: Int, b: Int): Int = {
  if (a > b) {
    gcd(a-b, b)
  } else if (a == b) {
    return a
  } else {
    gcd(a, b-a)
  }
}

@main
def task_03: Unit = {
  printGcd(12, 3)
  printGcd(121,15)
}