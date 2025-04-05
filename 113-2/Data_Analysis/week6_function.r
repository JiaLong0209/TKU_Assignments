p <- function(...) {
  cat("------\n")
  cat(..., '\n\n')
}

set.seed(42)

ex1 <- function(){

  fib_optimized <- function(n, memo = c(0, 1)) {
    if (length(memo) >= n + 1) return(memo[n + 1])
    memo[n + 1] <- fib_optimized(n - 1, memo) + fib_optimized(n - 2, memo)
    return(memo[n + 1])
  }
  
  p(fib_optimized(20))

  k <- function (b, h ){
    return (b*h) / 2
  }

  
  p(k(1:10, 3:12))
}


main <- function () {
  num = 1
  fun <- list(ex1)
  if (num == 0) {
    for (f in fun) {
      f()
    }
  }else {
    fun[[num]]()
  }
}

main()

