

def C(n, r):
    return 1 if (r == 0 or r == n) else C(n-1, r-1) + C(n-1, r)
    

def main():
    print(C(10, 9))

main()




