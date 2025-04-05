
p <- function(...) {
  print("------")
  print(...)
}

c1 <- c(105, 100 , 90, 84)
c2 <- c(102, 92, 110, 86)
c3 <- c(95, 120, 96, 88)

ex1 <- function () {

  a <- matrix(c(c1,c2,c3), 3, byrow=T)
  dimnames(a) <- list(c('zhongxiao', 'xinsheng', 'zhongshang'), c('fruit1', 'fruit2', 'fruit3', 'fruit4'))
  p('------------------------')
  p(a)

  # sum(a[1,])
  # sum(a[,1])
  p(rowSums(a))
  p(colSums(a))

}
ex1()

ex2 <- function () {
  a <- matrix(c(c1,c2,c3), 3, byrow=T)
  p(a)
  p(which(a > 100, arr.ind=T))
  p(which(a > 100, arr.ind=F))

}
ex2()




