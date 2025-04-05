p <- function(...) {
  print("------")
  print(...)
}

set.seed(42)

ex1 <- function(){
  name <- c("Wendy", "Joe", "Tom", "janice", "John")
  gender <- c("m", "f", "f", "m", "m")
  height <- sample(150:180, 5, replace=T)
  weight <- sample(40:100, 5, replace=T)

  df <- data.frame(name, gender, height, weight)

  p(df)

  p(df['height'][df['height']>160])

  p(df$height > 160)
  p(which(df['height']>160))
  p(df$height[which(df['height']>160)])

  p(df$height)
  p(df[1:5, 3])

  # p(which(df$gender == "f"))
  # p(df[df$gender=='f', ])

  # p(df[df$height>160, ])
  # p(df$height>160)

  p(df[df$height>170 & df$gender=='m', ])

  p(df[df$name %in% c("Wendy", "Tom"), ])
  # p(df[2])

  p(df[1])
  p(df[,1])
  p(df$name %in% c("Wendy", "Tom"), )
  p(names(df))
  p(rownames(df))
}

ex2 <- function(){
  name <- c("Wendy", "Joe", "Tom", "janice", "John")
  gender <- c("m", "f", "f", "m", "m")
  height <- sample(150:180, 5, replace=T)
  weight <- sample(40:100, 5, replace=T)

  df <- data.frame(name, gender, height, weight)

  p(df)

  new_df <- rbind(df, c('Jack', 'm', 174, 63), c('JJack', 'm', 174, 63))
  p(new_df)

  new_df[c(8,9), ] <- c("Elsa", "mary", 'm', 'm', 162, 160, 65, 55)
  p(new_df)   

  # age <- sample(10:20, 10, replace=T)
  # new_df <- cbind(new_df, age)
  new_df$age <- 1:9
  p(new_df)
  
}

ex3 <- function () {

  # load dataset 
  data()

  p(head(iris, 10))
  # p(iris[20:30, ])

  p(str(iris))

  # a.
  p(mean(iris$Sepal.Width))
  p(mean(iris[, 2]))

  # b
  p(sum(iris[50, c(1, 3)]))
  p(sum(iris[50, c('Sepal.Length', 'Petal.Length')]))

  # c.
  p(mean(iris[iris$Species == "setosa", "Petal.Width"]))
  p(mean(iris[iris$Species == "setosa",]$Petal.Width))

  # d 
  # p(iris[(iris$Sepal.Width + iris$Petal.Width > 4.5)])

  # e
  p(colMeans(iris[1:15, 1:4]))
  # p(iris[1:15, 1:4])

}

main <- function () {
  ex1()
  # ex2()
  # ex3()
}

main()


