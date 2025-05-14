
p <- function(...) {
  cat("------\n")
  cat(..., '\n\n')
}

set.seed(42)


ex1 <- function(){
  
  # (a)
  x <- sample(1:6, 6000, replace=T)
  print(table(x))
  print(table(x) / length(x))
  
  # (b)
  S <- 3600
  count <- 0
  x <- sample(1:6, S, replace=T)
  y <- sample(1:6, S, replace=T)

  print(table(x+y) / S)
}


ex2 <- function(){
  
  midterm <- sample(0:100, 100, replace=T)
  final <- sample(0:100, 100, replace=T)

  df <- data.frame(midterm, final)

  print(head(df, 5))

  # (a)
  print(mean(df$midterm))
  print(var(df$midterm))
  print(sd(df$midterm))

  # (b)
  print(cor(df$midterm, df$final))

  # (c)
  
  x <- df$midterm
  y <- df$final
  
  df['semester'] <- (x+y) / 2
  print(which(df$semester > 60))
  print(length(which(df$semester > 60)))

  print(as.numeric(rownames(df)[which(df$semester > 60)]))

  # (d)


  # print(df[df$midterm ])
  print(nrow(df[seq(1, 100, 2),] < 60))

  print((df[seq(1, 100, 2),] < 60))
  
}

ex3 <- function(){
  # options(scipen = 999)

  levels = c('f', 'm') # 1 2 3
  age <- sample(20:90, 10, replace=T)
  gender <- sample(levels, 10, replace=T)

  index <- c(NA, sample(30: 60, 9, replace=T))

  s_levels = c("Bad", "Normal", "Good")

  s <- sample(s_levels, 10, replace=T)

  fac <- factor(s, levels = s_levels, ordered=T)

  df <- data.frame(age, gender, index, fac)
  
  print(fac)

  print(df)
  print(str(df))

  # print(df$age[df$fac >= "Normal", ])
  print(df[c(1,3), c(1,2)])
  # print(nrow(df[df$fac >= "Normal", ]))
  #
  # print(as.numeric(df$fac) >= 2)
  #
  # # print(df[df$age >= 40, ])
  # print(mean(df[df$age >= 40, ], na.rm =T))

  # ord_fac <- factor(a, levels=c('yes', 'no', 'None'), labels = c('n', 'y', 'N'), ordered=T)
  # print(ordered(fac))
  #
  # print(ord_fac)
  #
}

# factor
ex4 <- function(){
  dates <- sample()
  dates <- sample()
  
  i <- c('shift',' pants','jacket')
  
  DataTime <- as.POSIXct(c('2018-11-12 04:00', '2018'))

  # readcsv("")
  # getwd("")
  # savewd("")

}

ex5 <- function(){

  levels = c('f', 'm') # 1 2 3
  age <- sample(20:90, 10, replace=T)
  gender <- sample(levels, 10, replace=T)
  index <- c(NA, sample(30: 60, 9, replace=T))
  s_levels = c("Bad", "Normal", "Good")
  s <- sample(s_levels, 10, replace=T)
  fac <- factor(s, levels = s_levels, ordered=T)
  df <- data.frame(age, gender, index, fac)

  print(getwd())
  path <- "./data/df.csv"
  write.csv(df, path)

}

ex6 <- function(){
  df <- read.csv("./data/df.csv")
  # library(openxlsx)
  # a <- read.xlsx()

  display(df)

}

main <- function () {

  num = 6

  fun <- list(ex1, ex2, ex3, ex4, ex5, ex6)
  if (num == 0) {
    for (f in fun) {
      f()
    }
  }else {
    fun[[num]]()
  }
}



main()








