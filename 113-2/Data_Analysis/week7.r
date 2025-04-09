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

# ifelse
ex2 <- function() {
  # c <- 3:20
  # p(c)

  dice.sum <- sum(sample(1:6, 3, replace =T))
  p(dice.sum)

  ifelse(dice.sum > 13, print('Good'), print('Bad'))

}

# 5.
ex3 <- function(){
  #
  # compute.weight <- function(gender, height){
  #   ifelse(gender=='m', (height-80)*0.7, (height-70)*0.6)
  # }

  compute.weight <- function(gender, height){
    (height-(70+gender*10)) * (0.6 + gender*0.1)
  }

  p(compute.weight(1, 160))
  p(compute.weight(0, 160))
  
}

# 9.
ex4 <- function(){
  # scores = (chinese, english, math)
  # score_judgement <- function(scores){
  #   weights = c(4, 6, 4)
  #   weighted_scores = (scores * weights) / sum(weights)
  #   sum_weighted_scores = sum(weighted_scores)
  #   cat(sum_weighted_scores, " ")
  #   ifelse(sum_weighted_scores >= 85, print('Good'), ifelse(sum_weighted_scores >= 60, print("Normal"), print("Bad")))
  # }
  #
  score_judgement <- function(scores){
    weights = c(4,6,4)
    sum_ws = sum(scores * weights / sum(weights))
    ifelse(sum_ws >= 85, print('Good'), ifelse(sum_ws >= 60, print("Normal"), print("Bad")))
  }

  scores = c(60, 30, 90)
  score_judgement(scores)
  score_judgement(c(90,100,60))
  score_judgement(c(60,60,0))

  9487
}

# for loop
ex5 <- function(){
  for (i in 1:3) {
    assign(paste0("var", i), i * 100)
  }

  p(ls())
  print(var1)  # 100
  print(var2)  # 200
  print(var3)  # 300

  for (i in 1:5){
    cat(1:i, '\n')
  }

  for (i in seq(1, 9, 2)){
    for (j in 1:i){
      cat(ifelse(j!=i, i, paste(i, '\n')))
    }
  }
  cat('\n')

  for (i in seq(1, 9, 2)){
    cat(rep(i, i), '\n')
  }

  cat('\n')

  for (i in seq(2, 8, 2)){
    cat(rep(i, 5), '\n')
  }

}

ex6 <- function(){
  x <- sample(1:30, 10, replace=T)
  for(i in x){
    cat(i, ifelse(i%%2, "odd", "even"), '\n')
  }

  ifelse(x%%2, "odd", "even")

}

# 2. 50 data
ex7 <- function(){
  score <- sample(0: 100, 50, replace = T)
  print(score)
  adjust_score <- function(score){

    max_score <- max(score)
    before_fail <- sum(score < 60) / length(score)
    alter_score <- (score ^ 0.5) * 10
    max_alter_score <- max(alter_score)
    alter_fail <- sum(alter_score < 60) / length(alter_score)

    cat(before_fail, '\n')
    cat(max_score, '\n')
    cat(alter_fail, '\n')
    cat(max_alter_score, '\n')

  }
  adjust_score(score)
}

ex8 <- function(){
  repeat{
    dice <- sample(1:6, 1)
    print(dice)
    if(dice == 2) break
  }
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

