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

