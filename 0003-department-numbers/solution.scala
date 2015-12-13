
object Solution {

	def main(args: Array[String]) {
		for (x <- departmentNumbers()) {
			println(x)
		}
	}

	def areDifferent(x:Int, y:Int, z:Int) : Boolean = {
		x != y && x != z && y != z
	}

	def isEven(n:Int) : Boolean = {
		n % 2 == 0		
	}

	def sumTo12(x:Int, y:Int, z:Int) : Boolean = {
		(x + y + z) == 12
	}

	def permutations(from:Int, to:Int) = {
		var result = List[Tuple3[Int, Int, Int]]()
		for (x <- from to to) {
			for (y <- from to to) {
				for (z <- 1 to 7) {
					result = (x, y, z) :: result
				}
			}
		}
		result

	}

	def departmentNumbers() = {
		val tuples = permutations(1, 7)
		tuples.filter((t:Tuple3[Int, Int, Int]) => areDifferent(t._1, t._2, t._3) && isEven(t._3) && sumTo12(t._1, t._2, t._3))
	}

}
