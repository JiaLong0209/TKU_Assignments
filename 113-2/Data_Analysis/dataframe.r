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

  p(which(df['height']>160))

  p(df$height)
  p(df[1:5, 3])

  # p(which(df$gender == "f"))
  # p(df[df$gender=='f', ])

  # p(df[df$height>160, ])
  # p(df$height>160)

  p(df[df$height>170 & df$gender=='m', ])

  p(df[df$name %in% c("Wendy", "Tom"), ])
  # p(df[2])
}
# ex1()

ex2 <- function(){
  name <- c("Wendy", "Joe", "Tom", "janice", "John")
  gender <- c("m", "f", "f", "m", "m")
  height <- sample(150:180, 5, replace=T)
  weight <- sample(40:100, 5, replace=T)

  df <- data.frame(name, gender, height, weight)

  p(df)

  new_df <- rbind(df, c('Jack', 'm', 174, 63))
  p(new_df)


}
ex2()
