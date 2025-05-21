
p <- function(...) {
  cat("------\n")
  cat(..., '\n\n')
}

set.seed(42)


ex1 <- function(){
  library(MASS)
  df <- Cars93
  k <- sort(table(df$Cylinders), decreasing = T)
  print(k)
  print(max(k))

  # las = 1: horizontal
  mid <- barplot(k, col = 2:7, ylim = c(0, max(k) + 2), las = 2,  cex.names = 1.2)
  text(x = mid, y = k + 1.5, labels = k, cex = 0.8, col = "black")
  print(mid)
}

ex2 <- function(){
  library(MASS)
  df <- Cars93
  k <- table(df$AirBags, df$Origin)
  print(k)
  print(max(k))

  mid_vert <- barplot(k, col = c(2,3,5), legend.text = T, args.legend = list(x = "topright", cex = 0.8), beside = T,  ylim = c(0, max(k) + 2), las = 1,  cex.names = 1.2)
  text(x = mid_vert, y = k + 0.5, labels = k, cex = 0.8, col = "black")

  mid_hori <- barplot(k, col = c(2,3,5), legend.text = T, args.legend = list(x = "bottomright", cex = 0.8), beside = T,  xlim = c(0, max(k) + 2), las = 1,  cex.names = 1.2, horiz= T)
  text(x = k + 0.5, y = mid_hori, labels = k, cex = 0.8, col = "black")

  print(mid_hori)
  
}

ex3 <- function(){
  library(MASS)
  df <- Cars93
  k <- table(df$Origin, df$AirBags)

  label_pos <- apply(k, 2, cumsum) - k/2
  print(k)
  print(max(k))
  print(label_pos)
  
}

# mapply
ex4 <- function(){
  library(MASS)
  attach(Cars93)
  install(plotrix)

  library(plotrix)
  cols = list(2:3, 4:6, 7:9)
  sizetree(Cars93[, c()], col=cols, showval=T, showcount=T, stacklabels=T, border="black", base.cex = 1.1)

}



ex5 <- function(){

  library(MASS)
  attach(Cars93)

  # category ~ nunmeric
  # category ~ category
  cols = 5:7
  plot(AirBags ~ Origin, col = cols)
  plot(AirBags ~ Price, col = cols)
  plot(Price ~ AirBags, col = cols)
  plot(AirBags,  Origin, col = cols)
  mosaicplot(~ DriveTrain + AirBags + Origin + Cylinders, col = 5:6)

  print(str(Cars93))
  print(AirBags ~ Price)
}


# install.packages("SciViews")
ex6 <- function(){
  library(MASS)
  attach(Cars93)
  library(SciViews)
  pairs(Cars93[,c("Origin", "Price", "Horsepower", Pri)], gap = 0.2, diag.panel=panel.hist, upper.panel = panel.cor)
}

# set operation
library(MASS)
ex7 <- function(){
  
  df <- Cars93
  # print(is.na(df))
  # print(na.omit(df))
  # print(complete.cases(df))

  print(df[, "Luggage.room"])
  k <- which(is.na(df$Luggage.room))
  print(df[is.na(df$Luggage.room), "Luggage.room"])

  # df[is.na(df$Luggage.room), "Luggage.room"] <- mean(df$Luggage.room, na.rm=T)
  df[is.na(df$Luggage.room), "Luggage.room"] <- mean(df$Luggage.room[-k])

  print(df[16, "Luggage.room"])

  # df$Luggage.room[is.na(df$Luggage.room),] <- mean(df$Luggage.room, na.rm = T)
}


ex8 <- function(){
  library(MASS)
  # ? Cars93
  df <- Cars93
  str(df)
  print(df[20:30, ])


}


main <- function () {

  num = 7
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








