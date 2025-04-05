p <- function(...) {
  print("------")
  print(...)
}

set.seed(42)

ex1 <- function(){
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

# histogram
ex2 <- function(){
  df <- iris
  # y = Frequence
  # hist(df$Sepal.Width)

  # y = Density
  # hist(df$Sepal.Width, breaks=c(0.5, 2.3, 5))

  # y = Frequence
  # hist(df$Sepal.Width, breaks=c(0.5, 2.3, 5), freq=T)

  # hist(df$Sepal.Width, breaks=c(0.5, 2.3, 3, 3.5, 5), freq=T, labels=c('a', 'b', 'c', 'd', 'e'), col = 1:5)

  # hist(df$Sepal.Width, breaks=c(0.5, 2.3, 3, 3.5, 5), freq=T, labels=T, col = 1:5)

  hist(df$Sepal.Width, breaks=c(0.5, 2.3, 3, 3.5, 5), freq=F, labels=T, col = 1:5, main="Test")
}

# Normal QQ Plot
ex3 <- function(){ 
  library(MASS)
  df <- crabs
  qqnorm(df$FL)
  qqline(df$FL)

  p(shapiro.test(df$FL))
#         Shapiro-Wilk normality test
# data:  df$FL
# W = 0.99037, p-value = 0.2023
}

# box plot
ex4 <- function(){
  df <- InsectSprays
  str(df)
  
  # boxplot(df$count)

  # boxplot(variables ~ categories)
  boxplot(count ~ spray, data = df)

  # include outlier
  boxplot(count ~ spray, data = df, range=0)

  boxplot(count ~ spray, data = df, range=0, col=2:7)

}

ex5 <- function(){
  df <- iris
  k <- boxplot(df$Sepal.Length)
  p(k$stats)
  text(y=k$stats, labels=k$stats, x=1)

  k <- boxplot(df$Sepal.Length ~ df$Species, col=2:4)
  p(k$stats)
  for (i in 1:3){
    text(y=k$stats[, i], x=i)
  }

  p(k$stats[, 1])
  p(k$stats[2,3])
}

# barplot : must be frequence table
ex6 <- function(){
  df <- mtcars
  g.table <- table(df$gear)
  p(g.table)
  k <- barplot(g.table, col=3:5, ylim=c(0, 20))
  text(x=k, y=g.table + 0.5, labels=g.table)

  k <- barplot(g.table, col=3:5, ylim=c(0, 20), name.arg=c('one', 'two', 'three'))
  text(x=k, y=g.table + 0.5, labels=g.table)
}

# cex: size, col: color
ex7 <- function(){
  df <- iris
  attach(df)
  # plot(Sepal.Length, Sepal.Width)
  plot(Sepal.Length, Sepal.Width, main="Scatter", xlab='SL', ylab="SW")
  plot(Sepal.Length, Sepal.Width, main="Scatter", xlab='SL', ylab="SW", cex=1.5)
  plot(Sepal.Length, Sepal.Width, main="Scatter", xlab='SL', ylab="SW", cex=1.5, col=2)
  plot(Sepal.Length, Sepal.Width, main="Scatter", xlab='SL', ylab="SW", cex=1.5, col=2, col.main=5, cex.lab=1.5)
  plot(Sepal.Length, Sepal.Width, main="Scatter", xlab='SL', ylab="SW", cex=1.5, col=2, col.main=5, cex.lab=1.5, col.lab= 4)
}

# par(): fg, bg, fig, 
ex8 <- function(){
  df <- iris
  attach(df)
  par(bg="#f15ac0", fg="blue")

  par(fig=c(0, 0.5, 0, 0.5))

  plot(Sepal.Length, Sepal.Width, main="Scatter", xlab='SL', ylab="SW", cex=1.5, col=2, col.main=5, cex.lab=1.5, col.lab= 4)

  par(fig=c(0.5, 1, 0.5, 1), mai=c(0.5, 1, 0.5, 1))

  df <- mtcars
  g.table <- table(df$gear)
  p(g.table)
  k <- barplot(g.table, ylim=c(0, 20))
  text(x=k, y=g.table + 0.5, labels=g.table)
}

# test 1
ex9 <- function(){
  # 1
  df <- mtcars

  k <- df$disp
  p(k)
  p(cut(k, 3))

  # 2
  p(table(df$gear))

  # 3
  plot(df$mpg, df$disp)

  # 4
  # hist(df$mpg, breaks=())
  
}

# pie char 
ex10 <- function(){
  df <- mtcars
  g.table <- table(df$gear)
  pie(g.table)

  per.gear <- paste(round(100 * g.table / sum(g.table), 2), '%')

  pie(g.table, labels=per.gear, col=2:4, main="frequency")
  # legend('topright', names<-c(3,4,5), fill=col<-2:4)
}

main <- function () {
  num = 10
  fun <- list(ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10)
  if (num == 0) {
    for (f in fun) {
      f()
    }
  }else {
    fun[[num]]()
  }
}

main()

