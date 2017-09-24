import math._
import scala.util._

object Solution extends App {
    val n = readInt
    println(math.ceil((-1+math.sqrt(1+8*n))/2).toInt)
}
