p <- function(...) {
  print("------")
  print(...)
}

set.seed(42)

# 1. 
ex1 <- function(){
  score <- c(NA, 0:100)
  math <- sample(score, 50, replace=T)
  english <- sample(score, 50, replace=T)
  chinese <- sample(score, 50, replace=T)

  my.score  <- data.frame(math, english, chinese, row.names = paste0("S", 1:50))
  p(head(my.score,10))
  failed <- my.score[my.score$math < 60 & my.score$english < 60 & my.score$chinese < 60  , ]
  p(failed)
}

ex2 <- function () {

  # load dataset 
  data()
  p(head(iris, 10))

  p(str(iris))

  # a.
  p(mean(iris$Sepal.Width))
  p(mean(iris[, 2]))

  # b
  # p(sum(iris[50, c(1, 3)]))
  p(sum(iris[50, c('Sepal.Length', 'Petal.Length')]))

  # c.
  p(mean(iris[iris$Species == "setosa", "Petal.Width"]))
  # p(mean(iris[iris$Species == "setosa",]$Petal.Width))

  # d 
  p(iris[iris$Sepal.Width + iris$Petal.Width > 4.5, ])

  # e
  p(colMeans(iris[1:15, 1:4]))
  # p(iris[1:15, 1:4])

}

ex3 <- function () {
  students <- c("Bruckner", "Cairger", "Mendoza", "Jaleela",
                "Williams", "Rida", "kai", "Jaabir", "Garces", "trevor")
  classes <- c('c', 'a', 'a', 'c', 'b', 'b', 'c', 'c', 'b', 'a')
  math_scores <- sample(20:100, 10, replace=T)
  english_scores <- sample(20:100, 10, replace=T)
  
  # a 
  Class.Score <- data.frame(Class = classes, Math = math_scores,
                            English = english_scores, row.names = students)

  print(Class.Score)
  # b. 
  Class.Score$Pass <- rowMeans(Class.Score[, c("Math", "English")]) >= 60
  print(Class.Score)
  
}

ex4 <- function(){
  scores <- c(30, 49, 95, NA, 54, NA, 61, 85, 51, 22, 0, 0)
  genders <- c('m', 'f', 'f', 'm', 'f', 'm', 'f', 'm', 'm', 'f', 'f', 'm')

  # a 

  p(length(scores))
  p(sum(genders == 'm'))
  p(sum(genders == 'f'))

  # b
  p(max(scores, na.rm = T))
  p(min(scores, na.rm = T))

  # c
  p(mean(scores, na.rm = T))
  p(sd(scores, na.rm = T))

  p(mean(scores[genders == 'm'], na.rm = T))
  p(mean(scores[genders == 'f'], na.rm = T))

  # d 
  p(scores)
  adjusted_scores <- ifelse(is.na(scores), 0, sqrt(scores) * 10)
  p(adjusted_scores)
  
  # e 
  passing_stu <- which(adjusted_scores >= 60)
  num_passing <- length(passing_stu)
  p(passing_stu)
  p(num_passing)

}

main <- function () {
  num = 0
  fun <- list(ex1, ex2, ex3, ex4)
  if (num == 0) {
    for (f in fun) {
      f()
    }
  }else {
    fun[[num]]()
  }
  
}

main()


# output:

# [1] "------"
#     math english chinese
# S1    47      47      79
# S2    99      24      71
# S3    63       4      83
# S4    23       4      41
# S5    72       0      56
# S6    98       1      70
# S7    16      19      27
# S8    47       0      53
# S9    45     100      36
# S10   22      56      NA
# [1] "------"
#     math english chinese
# S4    23       4      41
# S7    16      19      27
# S8    47       0      53
# NA    NA      NA      NA
# S15   18      47      53
# S18   39      27      41
# S24    3      14      23
# S29   56       0       4
# S31   40      22      41
# S35   13      38      29
# S36   20      19      32
# S45    2      52      13
# S47   48      30      40
# [1] "------"
#    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
# 1           5.1         3.5          1.4         0.2  setosa
# 2           4.9         3.0          1.4         0.2  setosa
# 3           4.7         3.2          1.3         0.2  setosa
# 4           4.6         3.1          1.5         0.2  setosa
# 5           5.0         3.6          1.4         0.2  setosa
# 6           5.4         3.9          1.7         0.4  setosa
# 7           4.6         3.4          1.4         0.3  setosa
# 8           5.0         3.4          1.5         0.2  setosa
# 9           4.4         2.9          1.4         0.2  setosa
# 10          4.9         3.1          1.5         0.1  setosa
# [1] "------"
# 'data.frame':   150 obs. of  5 variables:
#  $ Sepal.Length: num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ...
#  $ Sepal.Width : num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ...
#  $ Petal.Length: num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ...
#  $ Petal.Width : num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ...
#  $ Species     : Factor w/ 3 levels "setosa","versicolor",..: 1 1 1 1 1 1 1 1 1 1 ...
# NULL
# [1] "------"
# [1] 3.057333
# [1] "------"
# [1] 3.057333
# [1] "------"
# [1] 6.4
# [1] "------"
# [1] 0.246
# [1] "------"
#     Sepal.Length Sepal.Width Petal.Length Petal.Width    Species
# 16           5.7         4.4          1.5         0.4     setosa
# 51           7.0         3.2          4.7         1.4 versicolor
# 52           6.4         3.2          4.5         1.5 versicolor
# 53           6.9         3.1          4.9         1.5 versicolor
# 57           6.3         3.3          4.7         1.6 versicolor
# 71           5.9         3.2          4.8         1.8 versicolor
# 78           6.7         3.0          5.0         1.7 versicolor
# 86           6.0         3.4          4.5         1.6 versicolor
# 87           6.7         3.1          4.7         1.5 versicolor
# 101          6.3         3.3          6.0         2.5  virginica
# 102          5.8         2.7          5.1         1.9  virginica
# 103          7.1         3.0          5.9         2.1  virginica
# 104          6.3         2.9          5.6         1.8  virginica
# 105          6.5         3.0          5.8         2.2  virginica
# 106          7.6         3.0          6.6         2.1  virginica
# 108          7.3         2.9          6.3         1.8  virginica
# 110          7.2         3.6          6.1         2.5  virginica
# 111          6.5         3.2          5.1         2.0  virginica
# 112          6.4         2.7          5.3         1.9  virginica
# 113          6.8         3.0          5.5         2.1  virginica
# 115          5.8         2.8          5.1         2.4  virginica
# 116          6.4         3.2          5.3         2.3  virginica
# 117          6.5         3.0          5.5         1.8  virginica
# 118          7.7         3.8          6.7         2.2  virginica
# 119          7.7         2.6          6.9         2.3  virginica
# 121          6.9         3.2          5.7         2.3  virginica
# 122          5.6         2.8          4.9         2.0  virginica
# 123          7.7         2.8          6.7         2.0  virginica
# 125          6.7         3.3          5.7         2.1  virginica
# 126          7.2         3.2          6.0         1.8  virginica
# 127          6.2         2.8          4.8         1.8  virginica
# 128          6.1         3.0          4.9         1.8  virginica
# 129          6.4         2.8          5.6         2.1  virginica
# 130          7.2         3.0          5.8         1.6  virginica
# 131          7.4         2.8          6.1         1.9  virginica
# 132          7.9         3.8          6.4         2.0  virginica
# 133          6.4         2.8          5.6         2.2  virginica
# 136          7.7         3.0          6.1         2.3  virginica
# 137          6.3         3.4          5.6         2.4  virginica
# 138          6.4         3.1          5.5         1.8  virginica
# 139          6.0         3.0          4.8         1.8  virginica
# 140          6.9         3.1          5.4         2.1  virginica
# 141          6.7         3.1          5.6         2.4  virginica
# 142          6.9         3.1          5.1         2.3  virginica
# 143          5.8         2.7          5.1         1.9  virginica
# 144          6.8         3.2          5.9         2.3  virginica
# 145          6.7         3.3          5.7         2.5  virginica
# 146          6.7         3.0          5.2         2.3  virginica
# 148          6.5         3.0          5.2         2.0  virginica
# 149          6.2         3.4          5.4         2.3  virginica
# 150          5.9         3.0          5.1         1.8  virginica
# [1] "------"
# Sepal.Length  Sepal.Width Petal.Length  Petal.Width 
#     4.913333     3.346667     1.420000     0.200000 
#          Class Math English
# Bruckner     c   45      53
# Cairger      a   60      85
# Mendoza      a   84      51
# Jaleela      c   85      46
# Williams     b   75      29
# Rida         b   43      76
# kai          c   44      47
# Jaabir       c   80      56
# Garces       b   81      29
# trevor       a   33      24
#          Class Math English  Pass
# Bruckner     c   45      53 FALSE
# Cairger      a   60      85  TRUE
# Mendoza      a   84      51  TRUE
# Jaleela      c   85      46  TRUE
# Williams     b   75      29 FALSE
# Rida         b   43      76 FALSE
# kai          c   44      47 FALSE
# Jaabir       c   80      56  TRUE
# Garces       b   81      29 FALSE
# trevor       a   33      24 FALSE
# [1] "------"
# [1] 12
# [1] "------"
# [1] 6
# [1] "------"
# [1] 6
# [1] "------"
# [1] 95
# [1] "------"
# [1] 0
# [1] "------"
# [1] 44.7
# [1] "------"
# [1] 32.13185
# [1] "------"
# [1] 41.5
# [1] "------"
# [1] 46.83333
# [1] "------"
#  [1] 30 49 95 NA 54 NA 61 85 51 22  0  0
# [1] "------"
#  [1] 54.77226 70.00000 97.46794  0.00000 73.48469  0.00000 78.10250 92.19544
#  [9] 71.41428 46.90416  0.00000  0.00000
# [1] "------"
# [1] 2 3 5 7 8 9
# [1] "------"
# [1] 6
