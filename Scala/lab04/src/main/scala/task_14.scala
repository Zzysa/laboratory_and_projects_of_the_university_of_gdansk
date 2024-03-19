type Pred[A] = A => Boolean

val isEven: Pred[Int] = _ % 2 == 0
val isPositive: Pred[Int] = _ > 0

def or[A](p: Pred[A], q: Pred[A]): Pred[A] = {
    a => p(a) || q(a)
}

def and[A](p: Pred[A], q: Pred[A]): Pred[A] = {
    a => p(a) && q(a)
}

def not[A](p: Pred[A]): Pred[A] = {
    a => !p(a)
}

def imp[A](p: Pred[A], q: Pred[A]): Pred[A] = {
    a => !p(a) || q(a)
} 

val isEvenOrPositive = or(isEven, isPositive)
val isEvenAndPositive = and(isEven, isPositive)
val isNotEven = not(isEven)
val isImpfromEvenToPositive = imp(isEven, isPositive)

@main
def tast_14: Unit = {
    println(isEvenOrPositive(9))
    println(isEvenAndPositive(9))
    println(isNotEven(10))
    println(isImpfromEvenToPositive(9))
}
