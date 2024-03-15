def shuffle(l1: List[Int], l2: List[Int]): List[Int] = {
    @annotation.tailrec
    def helper(l1: List[Int], l2: List[Int], result: List[Int] = Nil): List[Int] = {
        if (l1.isEmpty && l2.isEmpty){
            result
        } else if (l1.isEmpty) {
            helper(l1, l2.tail, result :+ l2.head)
        } else if (l2.isEmpty) {
            helper(l1.tail, l2, result :+ l1.head)
        } else {
            if (l1.head == l2.head) {
                if (result != Nil) {
                    if (l1.head == result.last) {
                        helper(l1.tail, l2.tail, result)
                    } else {
                        helper(l1.tail, l2.tail, result :+ l2.head) 
                    }
                } else {
                    helper(l1.tail, l2.tail, result :+ l2.head) 
                }      
            } else if (l1.head > l2.head) {
                if (result != Nil) {
                    if (l2.head == result.last) {
                        helper(l1, l2.tail, result)
                    } else {
                        helper(l1, l2.tail, result :+ l2.head)   
                    }
                } else {
                    helper(l1.tail, l2.tail, result :+ l2.head) 
                }
            } else {
                if (result != Nil) {
                    if (l2.head == result.last) {
                        helper(l1.tail, l2, result)
                    } else {
                        helper(l1.tail, l2, result :+ l1.head)
                    }
                } else {
                    helper(l1.tail, l2, result :+ l1.head) 
                }
            }
        }      
    }
    
    helper(l1, l2)
}

val list1 = List(2,4,3,5)
val list2 = List(1,2,2,3,1,5)

val list3 = List(2, 4, 3, 5, 7)
val list4 = List(1, 2, 2, 3, 1, 5, 4)

@main
def task_09: Unit = {
    println(shuffle(list1, list2))
    println(shuffle(list3, list4))
    println(shuffle(list1, list3))

}
