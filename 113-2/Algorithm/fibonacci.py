def fibo(layer, n):
    global k 
    k, layer = k+1, layer+1
    print(f"k = {k:>4}\t l = {layer:>4}\t n = {n:>4}")
    return fibo(layer, n-1) + fibo(layer, n-2) if n>1 else n

def run_fibo():
    global k
    k = 0
    n = 6
    fibo(0, n)

run_fibo()

# output:
# k =    1         l =    1        n =    6
# k =    2         l =    2        n =    5
# k =    3         l =    3        n =    4
# k =    4         l =    4        n =    3
# k =    5         l =    5        n =    2
# k =    6         l =    6        n =    1
# k =    7         l =    6        n =    0
# k =    8         l =    5        n =    1
# k =    9         l =    4        n =    2
# k =   10         l =    5        n =    1
# k =   11         l =    5        n =    0
# k =   12         l =    3        n =    3
# k =   13         l =    4        n =    2
# k =   14         l =    5        n =    1
# k =   15         l =    5        n =    0
# k =   16         l =    4        n =    1
# k =   17         l =    2        n =    4
# k =   18         l =    3        n =    3
# k =   19         l =    4        n =    2
# k =   20         l =    5        n =    1
# k =   21         l =    5        n =    0
# k =   22         l =    4        n =    1
# k =   23         l =    3        n =    2
# k =   24         l =    4        n =    1
# k =   25         l =    4        n =    0


