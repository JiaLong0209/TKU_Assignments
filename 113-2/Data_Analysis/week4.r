p <- function(...) {
  print("------")
  print(...)
}

set.seed(42)

ex1 <- function(){
  data()
  df <- airquality
  is_complete <- complete.cases(df)

  p(is_complete)
  p(dim(df))

  # remove NA row
  p(dim(df[is_complete, ]))
  p(dim(na.omit(df)))
}

# Missing Value
ex2 <- function(){
  gender <- c("m", NA, "f", "m", "m")
  height <- c(sample(150:180, 4, replace=T), NA)
  weight <- sample(40:100, 5, replace=T)
  blood <- c("A", "A", NA, "O", NA)

  df <- data.frame(gender, height, weight, blood)
  p(df)

  p(is.na(df))

  index.na.gender <- which(is.na(df$gender))
  p(index.na.gender) # indecs of NA in gender column
  index.na.height <- which(is.na(df$height))
  index.na.blood <- which(is.na(df$blood))

  p(which(is.na(df$weight)))
  p(which(is.na(df$blood)))

  df$gender[index.na.gender] <- 'm'
  df$height[index.na.height] <- mean(df$height, na.rm=T)
  df$blood[index.na.blood] <-  median(df$blood, na.rm=T)


  p(df)
}

# Outlier Value
ex3 <- function(){
  d <- c(40, 56, 36, 43, 54, 5, 55, 60, 58, 100)
  p(d)
  boxplot.stats(d)

# ouput:
# $stats [1] 36.0 40.0 54.5 58.0 60.0
# $n [1] 10
# $conf [1] 45.50648 63.49352
# $out [1]   5 100
}

# data split
ex4 <- function(){
  df <- mtcars
  p(head(df), 3)
  p(class(df))
  p(df$mpg)

  p(range(df$mpg))
  p(cut(df$mpg, 3, include.lowest=T)) # split data to 3 block, include lowerst = (3, 5] to [3, 5]
  p(cut(df$mpg, 3, include.lowest=T, labels=c("A","B", "C"))) 

  p(cut(df$mpg, breaks = c(0, 10, 20, max(df$mpg)), include.lowest=T))
}

# encode, recode
ex5 <- function(){
  # x <- rep(c(1,2,3), 3)
  # library(glue)
  # install.packages("car")
  # library(car)
  # p(x)
  # trying to use CRAN without setting a mirror
# Calls: main ... <Anonymous> -> install.packages -> startsWith -> contrib.url
# Execution halted

  # 1, 2 -> A;   3 -> B
  # recode(x, "c(1,2)='A'; 3='B'")

  score <- sample(0: 100, 10)
  p(score)
  p(cut(score, breaks=c(0, 60, 80, 100), labels=c('C', 'B', 'A')))
  
}

# Rescale
ex6 <- function () {
  # library(scales)
  a <- c(2, 26, 16, 23, 14, 5 ,25, 30 ,8, 18)

  rescale <- function(arr, to = c(0, 1)){
      min_value <- min(arr)
      max_value <- max(arr)
      scaled_arr <- (arr - min_value) / (max_value - min_value)
      result <- scaled_arr * (to[2] - to[1]) + to[1]
      return (result)
  } 

  p(rescale(a))
}

ex7 <- function (){
  # rank() : return ranks (position in sorted arr) of each element in x
  # order(): return the indices that would sort x (index position)
  a <- c(2, 26, 16, 23, 14, 5 ,25, 30 ,8, 18)
  p(a)
  p(sort(a))
  p(rank(a))
  p(order(a))

  b <- c(12, 18, 8, 4, 30 , 28, 15)
  p(b)
  p(sort(b))
  p(rank(b))
  p(order(b))
  
  df <- mtcars
  p(head(df, 5))
  p(sort(df$mpg))
  p(head(df[order(df$mpg, decreasing=T), ], 5))
}

main <- function () {
  num = 7
  fun <- list(ex1, ex2, ex3, ex4, ex5, ex6, ex7)
  fun[[num]]()
}

main()

