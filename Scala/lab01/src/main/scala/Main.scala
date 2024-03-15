
def top_bottom(text: String): String = {
  val array = text.split('\n')
  "*" * array.maxBy(s => s.length).length() + "****"
}

def left_right(text: String): Unit = {
  val array = text.split('\n')
  val max = array.maxBy(s => s.length).length()
  for ( s <- array) {
    println("* " + s + " " * (max - s.length()) + " *")
  }
}

def text: String = {
  "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\nLorem Ipsum has been the industry's\nstandard dummy text ever since the 1500s, when an unknown printer took a galley of type\nand scrambled it to make a type specimen book. It has survived not only five centuries,\nbut also the leap into electronic typesetting, remaining essentially unchanged.\nIt was popularised in the 1960s with the release of Letraset\nsheets containing Lorem Ipsum passages, and more recently with desktop publishing software\nlike Aldus PageMaker including versions of Lorem Ipsum."
}

def borders(text: String): Unit = {
  println(top_bottom(text))
  left_right(text)
  println(top_bottom(text))
}

@main
def mainProg: Unit = {
  borders(text)
}
