
p <- function(...) {
  cat("------\n")
  cat(..., '\n\n')
}

set.seed(42)


ex1 <- function(){
  a <- sample(200: 300, 10, replace=T)
  t <- ts(a, start=2000, end=2010)
  plot(t, lwd = 2, col = 'blue')
  x_axis <- time(t)
  axis(1, at = x_axis)
}


ex2 <- function(){
  a <- sample(200: 300, 12, replace=T)
  t <- ts(a, start=c(2016, 1), frequency=12)

  plot(t, lwd = 2, col = 'blue', xaxt = 'n')

  print(cycle(t))
  x_axis <- time(t)
  axis(1, at = x_axis, labels= cycle(t))
}

ex3 <- function(){
  # options(scipen = 999)
  a <- sample(500000: 500100, 11, replace=T)
  t <- ts(a, start=c(2016, 3), frequency=4)

  plot(t, lwd = 2, col = 'blue', xaxt = 'n')

  print(cycle(t))
  x_axis <- time(t)
  axis(1, at = x_axis)

}

# factor
ex4 <- function(){
  levels = c('no',"yes",  'None') # 1 2 3
  labels = c('N', 'Y' , "NN")
  a <- c("yes", 'no', 'yes', 'yes', 'no', 'yes')
  fac <- factor(a, levels = levels, labels = labels)
  
  print(a)
  print(fac)

  print(as.character(fac))
  print(as.numeric(fac))
  print(as.vector(fac))

  print(levels(fac))
  print(nlevels(fac))

  ord_fac <- factor(a, levels=c('yes', 'no', 'None'), labels = c('n', 'y', 'N'), ordered=T)
  print(ordered(fac))

  print(ord_fac)

}

main <- function () {

  num = 5
  fun <- list(ex1, ex2, ex3, ex4)
  if (num == 0) {
    for (f in fun) {
      f()
    }
  }else {
    fun[[num]]()
  }
}



main()








