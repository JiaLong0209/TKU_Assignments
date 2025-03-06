p <- function(...) {
  print('')
  print('--------')
  print(...)
}

c1 <- c(2,1,6,3,5,8)

# 4.(a)
ex1 <- function () {

  m <- matrix(c1, nrow=3, byrow=F)
  p(m)

  m <- matrix(c1, nrow=3, byrow=T)
  p(m)
}

# 4.(b)
ex2 <- function() {
  no1 <- c(2,3)
  no2 <- c(1.5)
  no3 <- c(6,8)
  m <- rbind(no1, no2, no3)
  p(m)

  colnames(m) <- c('var.1', 'var.2')
  p(m)
}

# 5.
ex3 <- function() {
  c1 <- c(105, 100 , 90, 84)
  c2 <- c(102, 92, 110, 86)
  c3 <- c(95, 120, 96, 88)

  a <- matrix(c(c1,c2,c3), 3, byrow=T)
  dimnames(a) <- list(c('zhongxiao', 'xinsheng', 'zhongshang'), c('fruit1', 'fruit2', 'fruit3', 'fruit4'))
  p(a)

  sum(a[1,])
  sum(a[,1])
  p(rowSums(a))
  p(colSums(a))
}

# 6.
ex4 <- function () {
  v1 <- c(80, 86, 90, 92, 80, 66, 62, 60, 64, 68, 56)
  v2 <- c(83, 87, 80, 96, 03, 82, 69, 65, 54, 61, 60, 54)
  
  cnames <- c('1st season', '2nd season',  '3rd season', '4th season')
  rnames <- c("COCO", '50lan', 'COMBUY')
  mnames <- c('Taipei', 'Xinpei')
  
  result <- array(c(v1, v2), dim = c(3,4,2),
                dimnames = list(rnames, cnames, mnames))

  p(result)

}

main <- function () {
  ex1()
  ex2()
  ex3()
  ex4()
}

main()


# output:
# [1] ""
# [1] "--------"
#      [,1] [,2]
# [1,]    2    3
# [2,]    1    5
# [3,]    6    8
# [1] ""
# [1] "--------"
#      [,1] [,2]
# [1,]    2    1
# [2,]    6    3
# [3,]    5    8
# [1] ""
# [1] "--------"
#     [,1] [,2]
# no1  2.0  3.0
# no2  1.5  1.5
# no3  6.0  8.0
# [1] ""
# [1] "--------"
#     var.1 var.2
# no1   2.0   3.0
# no2   1.5   1.5
# no3   6.0   8.0
# [1] ""
# [1] "--------"
#            fruit1 fruit2 fruit3 fruit4
# zhongxiao     105    100     90     84
# xinsheng      102     92    110     86
# zhongshang     95    120     96     88
# [1] ""
# [1] "--------"
#  zhongxiao   xinsheng zhongshang 
#        379        390        399 
# [1] ""
# [1] "--------"
# fruit1 fruit2 fruit3 fruit4 
#    302    312    296    258 
# [1] ""
# [1] "--------"
# , , Taipei
#
#        1st season 2nd season 3rd season 4th season
# COCO           80         92         62         68
# 50lan          86         80         60         56
# COMBUY         90         66         64         83
#
# , , Xinpei
#
#        1st season 2nd season 3rd season 4th season
# COCO           87          3         65         60
# 50lan          80         82         54         54
# COMBUY         96         69         61         80
#
