def change(d, n):
    count = 0
    for i in d:
        while(n >= i):
            count += 1
            n -= i
    return count 

n = 63
d = [1000, 500, 100, 50, 10, 5, 1]

print(change(d, n))

