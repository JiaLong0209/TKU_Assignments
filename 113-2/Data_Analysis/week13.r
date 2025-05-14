
p <- function(...) {
  cat("------\n")
  cat(..., '\n\n')
}

set.seed(42)


ex1 <- function(){
  m <- matrix(1:9, nrow =3)
  print(m)
  print(apply(m, 1, sum))
  print(apply(m, 2, sum))

  print(rowSums(m))
  print(colSums(m))

  for (i in 1:nrow(m)){
    cat(sum(m[i,]), ' ')
  }
}


ex2 <- function(){
  
  n <- 5
  math <- sample(0: 100, n, replace=T)
  physics <- sample(0: 100, n, replace=T)
  calculus <- sample(0: 100, n, replace=T)
  english <- sample(0: 100, n, replace=T)

  df <- data.frame(math, physics, calculus, english)
  print(df)

  print(apply(df[,1:4], 2, max))
  print(apply(df[,1:4], 1, mean))
  df$mean <-  apply(df[,1:4], 1, mean)
  print(df)

  
}

ex3 <- function(){
  a<-seq(2,10,2)
  b<- matrix(c(4,10,2,8), 2)

  l <- list(a = a, b = b)
  print(l)
  print(lapply(l, sum))
  print(lapply(l, function (x) x ** 2))
}

# mapply
ex4 <- function(){
  # print(mapply(rep, 1:3, 3:1)
  # print(rep(1:3, 3:1))

  first <- list(A=matrix(1:16, 4), B =matrix(1:16, 2))
  second <- list(A=matrix(1:16, 4), B =matrix(1:16, 8))
  print(mapply(identical, first, second))

  print(mapply(function(x,y) {
                 nrow(x)+nrow(y)}
               , first, second))

  a<- seq(1,5,2)
  b<- seq(2,6,2)

  print(mapply(function (x,y,z) {x*2 - y + z}
       , a, b, MoreArgs = list(z=c(11:13))))


}



ex5 <- function(){

  set.seed(42)
  sizes <- c(5, 10, 15)
  means <- c(0, 100, 1000)

  print(mapply(rnorm, n = sizes, mean = means, sd = 1))

  x <- 2:4
  y <- 3:1

  power_fun <- function(base, exp, k){
    (base ^ exp) * k
  }

  print(mapply(power_fun, x, y, MoreArgs = list(k = 10)))
}


# tapply (data, INDEX, FUN)
ex6 <- function(){
  data <- seq(10, 60, 10)

  
  n <- 10
  b <- c('A', 'AB', 'O')
  g <- c('F', 'M')

  id <- paste0('4127701',c(1:n))
  gender <- sample(g, n, replace=T)
  blood <- sample(b, n, replace=T)
  math <- sample(0: 100, n, replace=T)
  physics <- sample(0: 100, n, replace=T)
  calculus <- sample(0: 100, n, replace=T)
  english <- sample(0: 100, n, replace=T)

  df <- data.frame(id, gender, blood, math, physics, calculus, english)
  print(df)

  df$mean <-  apply(df[,4:7], 1, mean)
  print(df)

  print(tapply(df$math, list(df$blood, df$gender), mean))

  print(tapply(df$blood, df$blood, length))
  print(table(df$blood))
}

# set operation
ex7 <- function(){
  x <- 1:10
  y <- 5:30
  z <- c(x, 20:30)

  print(union(x, y))
  print(intersect(x, y))

  print(setdiff(x, y)) # x - y 
  print(setequal(x, y)) # x == y ? 
  print(is.element(3, x)) # 3 is in x ?
  print(x %in% y)

  print(is.element(x, y))

  print(Reduce(union, list(x, y ,z)))
  print(all(x %in% z))
  print(all(is.element(x, z)))
  
}


ex8 <- function(){
  library(MASS)
  # ? Cars93
  df <- Cars93
  str(df)
  print(df[20:30, ])


}


main <- function () {

  num = 8
  fun <- list(ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8)
  if (num == 0) {
    for (f in fun) {
      f()
    }
  }else {
    fun[[num]]()
  }
}



main()








