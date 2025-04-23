p <- function(...) {
  cat("------\n")
  cat(..., '\n\n')
}

set.seed(42)

# 1. student math, english, chinese scores
ex1 <- function(){
  set.seed(12345)
  score <- c(NA, 0:100)
  math <- sample(score, 50, replace=T)
  english <- sample(score, 50, replace=T)
  chinese <- sample(score, 50, replace=T)

  my.score <- data.frame(math, english, chinese, row.names = paste0("s", 1:50))
  my.score[is.na(my.score)] <- 0
  failed_stu <- my.score[rowSums(my.score <  60) >= 1, ]
  print(my.score)

  print(failed_stu)
  # print(rowSums(my.score <  60))

}

# 2. iris
ex2 <- function (){
  
  data()
  print(head(iris, 10))

  print(str(iris))

  # (a)
  print(mean(iris$Sepal.Width))
  print(mean(iris[, 2]))

  # (b)
  # print(sum(iris[50, c(1, 3)]))
  print(sum(iris[50, c('Sepal.Length', 'Petal.Length')]))

  # (c)
  print(mean(iris[iris$Species == "setosa", "Petal.Width"]))
  # print(mean(iris[iris$Species == "setosa",]$Petal.Width))

  # (d)
  print(iris[iris$Sepal.Width + iris$Petal.Width > 4.5, ])

  # (e)
  print(colMeans(iris[1:15, 1:4]))
  # print(iris[1:15, 1:4])

}

# 3. Three Class math and english score
ex3 <- function () {
  students <- c("Bruckner", "Cairger", "Mendoza", "Jaleela",
                "Williams", "Rida", "kai", "Jaabir", "Garces", "trevor")
  classes <- c('c', 'a', 'a', 'c', 'b', 'b', 'c', 'c', 'b', 'a')
  math_scores <- c(45, 33, 97, 71, 65, 39, 70, 54, 22, 48)
  english_scores <- c(79, 26, 99, 76, 98, 22, 85, 15, 60, 95)
  
  # a 
  Class.Score <- data.frame(Class = classes, Math = math_scores,
                            English = english_scores, row.names = students)

  print(Class.Score)
  # b. 
  Class.Score$Pass <- rowMeans(Class.Score[, c("Math", "English")]) >= 60
  print(Class.Score)
  
}

# 4. Student score and gender analysis
ex4 <- function(){
  scores <- c(30, 49, 95, NA, 54, NA, 61, 85, 51, 22, 0, 0)
  genders <- c('m', 'f', 'f', 'm', 'f', 'm', 'f', 'm', 'm', 'f', 'f', 'm')

  # a 
  print(length(scores))
  print(sum(genders == 'm'))
  print(sum(genders == 'f'))

  # b
  print(max(scores, na.rm = T))
  print(min(scores, na.rm = T))

  # c
  print(mean(scores, na.rm = T))
  print(sd(scores, na.rm = T))

  print(mean(scores[genders == 'm'], na.rm = T))
  print(mean(scores[genders == 'f'], na.rm = T))

  # d 
  print(scores)
  adjusted_scores <- ifelse(is.na(scores), 0, sqrt(scores) * 10)
  print(adjusted_scores)
  
  # e 
  passing_stu <- which(adjusted_scores >= 60)
  num_passing <- length(passing_stu)
  print(passing_stu)
  print(num_passing)

}

main <- function () {

  num = 1
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

