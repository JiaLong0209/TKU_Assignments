set.seed(42)

# 1. dice.sum
ex1 <- function() {
  roll_dice <- function(){
    dice.sum <- sum(sample(1:6, 3, replace =T))
    print(dice.sum)
    ifelse(dice.sum > 13, print('Good'), print('Bad'))
  }
  roll_dice()
}

# 2. 
ex2 <- function(){
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

# 3. 
ex3 <- function(){
  for (i in 1:5){
    cat(1:i, '\n')
  }

  cat('\n')
  for (i in seq(1, 9, 2)){
    cat(rep(i, i), '\n')
  }
}

# 4.
ex4 <- function(){
  orig.score <- sample(0:100, 55, replace = T)

  print(orig.score)
  adjustment <- function(scores, method){
    if(method == 1){
      adj.score <- ifelse(scores > 55 & scores < 60, 60, scores)
    }else if(method == 2){
      adj.score <- (scores ^ 0.5 ) * 10
    }
    return (adj.score)
  }

  final.score <- adjustment(orig.score, method=1)
  print(final.score)

  final.score <- adjustment(orig.score, method=2)
  print(final.score)
}

# 5.
ex5 <- function(){
  #
  compute.weight <- function(gender, height){
    ifelse(gender=='m', (height-80)*0.7, (height-70)*0.6)
  }

  # compute.weight <- function(gender, height){
  #   (height-(70+gender*10)) * (0.6 + gender*0.1)
  # }

  print(compute.weight('m', 160))
  print(compute.weight('f', 160))
  
}

# 9.
ex9 <- function(){

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
}

ex6 <- function(){
  x <- sample(1:30, 10, replace=T)
  for(i in x){
    cat(i, ifelse(i%%2, "odd", "even"), '\n')
  }

  ifelse(x%%2, "odd", "even")

}

main <- function () {

  num = 4
  fun <- list(ex1, ex2, ex3, ex4, ex5)
  if (num == 0) {
    for (f in fun) {
      f()
    }
  }else {
    fun[[num]]()
  }
}

main()

