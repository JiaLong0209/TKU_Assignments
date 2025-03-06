
# rep(c(2,4,1), c(3,4,5))
# rep(1:3, each=4, length.out=5)


hw <- function(){
# 1.
# (a)
  rep(2:6, 5:1)

# (b)
  seq(11, 51, 4)

# (c)
}

### 
test <- function(){
  cumprod(rep(2:6, 5:1))
  cumprod(cumprod(seq(11, 51, 4)))
}

### 
test2 <- function(){
  print(sample(2:100, 3))

  set.seed(123)
  print(sample(2:100, 3))
  set.seed(123)
  print(sample(2:100, 3))

  print(sample(0:10, 10, replace=T))
  print(sample(0:10, 10))
  print()

}

test3 <- function(){
  x <- sample(1:100, 10)
  print(sort(x))
  print(rev(x))
  print(rank(x))
  
  # print(letters())
  y <- c(12,30,50,90,13,63,77)
  print(y[y > 50])
  print(y[which(y > 50)])
  print(y[y %% 2 == 1])
}
test3()

