
object Solution {

	def main(args: Array[String]) {
		departmentNumbers()
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

	def departmentNumbers() = {
		for (x <- 1 to 7) {
			for (y <- 1 to 7) {
				for (z <- 1 to 7) {
					if (areDifferent(x, y, z) && isEven(z) && sumTo12(x, y, z))
						println(s"$x, $y, $z")
				}
			}
		}
	}


}
