
p <- function(...) {
  cat("------\n")
  cat(..., '\n\n')
}

set.seed(42)

# save jpeg
ex1 <- function(){
  # getwd()
  jpeg(filename="images/0.jpg")
  pie(1:4)
  dev.off()
}


ex2 <- function(){

  # partition
  print(getwd())
  par(mfrow=c(2, 2))
  attach(iris)

  hist(Sepal.Length)
  plot(Petal.Length, Petal.Width)
  boxplot(Sepal.Length)
  barplot(table(Species))

  jpeg(filename="images/2.jpg")
  dev.off()
}

saveimg <- function(name="image.jpg",wd="images"){
  path <- paste0(wd, '/', name)
  print(path)
  jpeg(filename=path)
  dev.off()
}


ex3 <- function(){
# 2行2列のレイアウト
  print(getwd())
  layout(matrix(c(1, 2, 3, 3), 2, 2, byrow = TRUE))

# 各プロット
  attach(iris)
  hist(Sepal.Length)
  plot(Petal.Length, Petal.Width)
  boxplot(Sepal.Length)
  # barplot(table(Species))

  saveimg()
}

ex4 <- function(){
# 2行2列のレイアウト
  print(getwd())
  layout(matrix(c(1,4,3,2), 2, 2), width=c(2,1), height=c(1,1))
  layout.show(4)

  layout(matrix(c(3, 1, 4, 2), 2, 2), width=c(2, 1), height=c(2, 1))
  layout.show(4)

  layout(matrix(c(1:6), 2, 3), width=c(1, 2, 1), height=c(1, 2))
  layout.show(6)

  layout(matrix(c(1:100), 10, 10), width=c(1, 2, 1, 3), height=c(5, 1, 2))
  layout.show(100)

  layout(matrix(c(1:2500), 50, 50), width=c(25:1, 1:25), height=c(25:1, 1:25))
  layout.show(2500)

}


ex5 <- function(){
  # plot(iris$Sepal.Length, iris$Sepal.Width)
  par(mfrow=c(1, 1), fig=c((1/3), (2/3), 0.5, 1))
  par(mfrow=c(1,1), fig=c(0.5, 1, 0, 0.5))
  layout.show(2)
}

# Date
ex6 <- function(){
  k.data<-as.Date("2015-03-12")

  print(k.data)
  print(str(k.data))
  print(k.data+c(10:20))
  print(weekdays(k.data+c(10:20)))

  a <- as.Date("2025-04-25")
  print(weekdays(a))
  print(months(a))

  print(quarters(a))

  print(Sys.Date())

  print(seq(a, by='3 year', length.out=10))
  print(seq(a, by='365 day', length.out=10))
  print(seq(a, as.Date("2026-01-01"), length.out=10))
}

# Sys
ex7 <- function(){
  print(Sys.time())
  print(Sys.time()+30) # add 30 seconds

  t <- as.POSIXct(Sys.time()) # 2025-04-25 10:41:45 CST
  print(t)
  str(t+1:30)
}

# time series: ts(data, start, end, frequency)
ex8 <- function(){
  num <- sample(1:100, 10, replace=T)
  t <- ts(num, 2000, 2000+length(num), 3)
  print(t)
  
  height <- sample(200:300, 12, replace=T)
  t <- ts(height, c(2016, 2), frequency=4)

  print(t)
  
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

