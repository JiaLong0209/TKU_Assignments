p <- function(...) {
  print("------")
  print(...)
}

set.seed(42)

ex1 <- function(){
  df <- mtcars
  k <- order(df$mpg)
  p(k)
  p(head(df[k, ]), 8)

  k <- order(df$gear, df$mpg)
  p(head(df[k, ]), 8)

  p((df[order(df$mpg, df$gear), ]))
  
}

# cbind(): new column
# rbind(): new row
# merge(): 

ex2 <- function() {
  id <- c('b1','a1', 'a2', 'a3')

  gender <- c('m', 'f', 'f', 'm')
  age <- sample(10:50, 4)
  income <- sample(1:1000, 4)

  edu<- c('bachelor', 'master', 'bachelor', 'master')
  exp <- sample(1:10, 4)
  a <- data.frame(gender, id, age, income)
  b <- data.frame(edu,id,  exp)
  p(a)
  p(b)
  p(merge(a,b ))

  # union
  p(merge(a,b, all=T))

  # intersaciton
  p(merge(a,b, all=F))

  # left join
  p(merge(a, b, all.x=T))

  # right join
  p(merge(a, b, all.y=T))
}

# sapply: apply function for each column
ex3 <- function(){
  library(MASS)
  df <- crabs
  # p(head(df))
  # str(df)
#  $ sp   : Factor w/ 2 levels "B","O": 1 1 1 1 1 1 1 1 1 1 ...
#  $ sex  : Factor w/ 2 levels "F","M": 2 2 2 2 2 2 2 2 2 2 ...
#  $ index: int  1 2 3 4 5 6 7 8 9 10 ...
#  $ FL   : num  8.1 8.8 9.2 9.6 9.8 10.8 11.1 11.6 11.8 11.8 ...
#  $ RW   : num  6.7 7.7 7.8 7.9 8 9 9.9 9.1 9.6 10.5 ...
#  $ CL   : num  16.1 18.1 19 20.1 20.3 23 23.8 24.5 24.2 25.2 ...
#  $ CW   : num  19 20.8 22.4 23.1 23 26.5 27.1 28.4 27.8 29.3 ...
#  $ BD   : num  7 7.4 7.7 8.2 8.2 9.8 9.8 10.4 9.7 10.3 ..

  p(colMeans(df[, 4:8]))
  p(sapply(df[, 4:8], function (x) return(mean(x)) ))
  p(sapply(df[, 4:8], function (x) range(x) ))
  p(sapply(df[, 4:8], quantile))

  p(quantile(df$FL, probs= c(0.1, 0.4, 0.9)))
  # mean
  p(sapply(df[, 4:8], function (x) {
             t <- 0
             for (n in x){
               t <- t + n
             }
             return (t / length(x))

} ))
  
  p(sapply(df[, 4:8], var)) # variance
  p(sapply(df[, 4:8], sd)) # std deviation

  summary(df)
  # p(df[, 4:8])
}


ex4 <- function(){
  df <- mtcars
  str(df)
#  $ mpg : num  21 21 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 ...
#  $ cyl : num  6 6 4 6 8 6 8 4 4 6 ...
#  $ disp: num  160 160 108 258 360 ...
#  $ hp  : num  110 110 93 110 175 105 245 62 95 123 ...
#  $ drat: num  3.9 3.9 3.85 3.08 3.15 2.76 3.21 3.69 3.92 3.92 ...
#  $ wt  : num  2.62 2.88 2.32 3.21 3.44 ...
#  $ qsec: num  16.5 17 18.6 19.4 17 ...
#  $ vs  : num  0 0 1 1 0 1 0 1 1 1 ...
#  $ am  : num  1 1 1 0 0 0 0 0 0 0 ...
#  $ gear: num  4 4 4 3 3 3 3 4 4 4 ...
#  $ carb: num  4 4 1 1 2 1 4 2 2 4 ...

  p(table(df$hp))

  # table(vertical, horizontal)

  # p(table(df$gear, df$hp))

  p(with(df, table(hp)))

  p(with(df, table(am, gear)))

  p(addmargins(with(df, table(am, gear))))

  # addmargins(data, 1 or 2) 1: display column sum, 2 display row sum
  p(addmargins(with(df, table(am, gear))), 2)
}

ex5 <- function(){
  df <- iris
  str(df)
# 'data.frame':   150 obs. of  5 variables:
#  $ Sepal.Length: num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ...
#  $ Sepal.Width : num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ...
#  $ Petal.Length: num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ...
#  $ Petal.Width : num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ...
#  $ Species     : Factor w/ 3 levels "setosa","versicolor",..: 1 1 1 1 1 1 1 1 1 1 ...
#
  # scatter plot: col = color, pch = plot style
  # plot(df$Petal.Length, df$Petal.Width, col = 'red', pch = 8)
  # with(df,  plot(Petal.Length, Petal.Width, col = 'black', pch=3))
  attach(df)
  # plot(Petal.Length, Petal.Width, col = '#1fe133', pch="$")
  # plot(Petal.Length, Petal.Width, col = 'black', pch="$", xlab='PL', ylab='PW', type='l')
  # plot(Petal.Length, Petal.Width, col = 'black', pch="$", xlab='PL', ylab='PW', type='h')

  # par()
  
  spe <- c("setosa","versicolor", "virginica")
  cols <- 2:4
  pchs <- 2:4

  f = c( "Sepal.Length", "Sepal.Width ", "Petal.Length", "Petal.Width ")

  a <- df[Species == spe[1], ]
  b <- df[Species == spe[2], ]
  c <- df[Species == spe[3], ]


  plot(a$f[3], a$f[4],col=cols[1], pch=pchs[1], xlim=c(0,100), ylim=c(0.5, 30))
  points(b$f[3], b$f[4], col=cols[2], pch=pchs[2])
  points(c$f[3], c$f[4], col=cols[3], pch=pchs[3])

  legend("topright", pch=pchs, col=cols, legend=spe)

  

}

main <- function () {
  num = 5
  fun <- list(ex1, ex2, ex3, ex4, ex5)
  fun[[num]]()
}

main()

