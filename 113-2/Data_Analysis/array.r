
p <- function(...) {
  print("------")
  print(...)
}

set.seed(42)
c1 <- 5:28
c2 <- array(sample(1: 10, 24, replace=T), dim=c(3,4,2))


ex1 <- function () {

  # dim = (i, j, k)
  a <- array(c1, dim=c(3,4,2))
  p(a)

  # p(a[2,3,2])
  # p(a[1, 1:3, 2])

  # p(a[, c(1, 4), 1])
  # p(a[c(1,3), 2:3, 2])
  p(a[-2, -3, -2])

}

ex1()

ex2 <- function(){
  a <- c2
  p(a)

}
# ex2()
