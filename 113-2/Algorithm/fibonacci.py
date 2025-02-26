def fibo(layer, n):
    global k 
    k, layer = k+1, layer+1
    print(f"k={k}, l={layer}, n={n}")
    return fibo(layer, n-1) + fibo(layer, n-2) if n>1 else n

def run_fibo():
    global k
    k = 0
    n = 4
    fibo(0, n)
run_fibo()

