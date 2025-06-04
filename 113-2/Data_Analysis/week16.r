
# strsplit
ex1 <- function(){
  
  min_max <- function(x){
  if(is.character){
    (return ("Input Error"))
  } else {
    print(max(x))
    print(min(x))
  }
  }

  min_max(c(35,12,5,6,2))



}

ex2 <- function(){
  a <- c(1,1,2,2,3,5,8,1)
  print(duplicated(a))

  print(which(duplicated(a)))
  print(a[-which(duplicated(a))])

  a <- c('A', 'B', 'C', 'D')
  b <- 10:13
  
  print(paste(a))
  print(paste('F', '000', a, collapse="|", seq="**"))
  print(paste(a, b))

  print(paste(1:5, collapse=''))
  print(
        sapply(strsplit(paste(1:5, collapse=''), ''),
          function (x) as.numeric(x)
        )
  )
  print(
        lapply(strsplit(paste(1:5, collapse=''), ''),
          function (x) as.numeric(x)
        )
  )
}

ex3 <- function(){
  s1 <- LETTERS[1:5]
  s2 <- letters[22:26]

  print(paste(s1, s2))
  # sep: seperate
  print(paste(s1, s2, sep='-', collapse= " | "))
  print(paste(s1, s2, sep='*', collapse= "%"))


  s1 <- rep(c('spade', 'heart', 'diamond', 'clab'), each=13)
  s2 <- c('A', 2:10, "J", "Q", "K")
  

  x <- paste(s1, s2, sep='')
  print(x)

  i <- grepl("A$", x)

  
  print(i)
  print(x[i])

  print(sample(x[!grepl("A$", x)], 1, ))

  
  colors = c("red", "yellow", "blue")
  print(colors)
  print(paste("I like", paste(colors, collapse=",")))
  print(paste("Red", colors))
}

# mapply
ex4 <- function(){
  d <- state.name
  substr(d, 1, 3)

  print(d)

  # grep return index
  i <- grep("^A|^F|g$", d)
  print(i)
  print(d[i])


  city <- c("TaipeiCity", "NewTaipeiCity", "KaohsiungCity")
  print(substr(city, 1, nchar(city)-4))
  
  l <- sample(LETTERS[1:5] , 20, replace=T)

  group <- mapply(function (x) ifelse(x=='A' || x=='B', "one", ifelse(x=="C", 'two', "three")), l)


  
  f1 <- factor(l,levels=sort(LETTERS[1:5], decreasing=T), ordered=T)

  f2 <- factor(group, levels=c('one', 'two', 'three'), ordered=T)

  print(f1)
  print(f2)

  df <- data.frame(f1, f2)
  print(df)
  str(df)
  # print()
  
  # library(car)
  # print(mapply(functin (x) ifelse())) )

  n <- 60
  ID <- sample(1:n)
  gender_level <- c("M", "F")
  gender <- sample(gender_level, n, replace=T)
  consent_level <- c("very bad", "bad", "normal", "good", "very good")
  consent <- sample(consent_level, n, replace=T, prob=c(1,1,2,10,2))
  print(consent)
  consent_factor <- factor(consent, levels=consent_level, ordered=T)

  print(consent_factor)

  print(table(consent))

  df <- data.frame(ID, gender, consent_factor)

  print(head(df, 5))

  ##
  print(df[df$consent_factor <= "bad", "ID"] )
  print(df$ID[df$consent_factor <= "bad"] )
   
  print(mean(as.numeric(consent_factor)))

  print(sum(1:5 * table(consent))/ 60)

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

  num = 4
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
