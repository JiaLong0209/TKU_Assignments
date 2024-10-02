from functools import reduce

def print_arr(a):
    print()
    for row in a:
        print(*row)

def product(a, b):
    return [[ reduce(lambda acc, cur:acc+cur, [a[i][k] * b[k][j] for k in range(len(a[0]))])  for j in range(len(b[0]))] for i in range(len(a))]
# 3 x 4
a = [[(i+1)*(j+1) for j in range(4)] for i in range(3)]

# 4 x 3
b = [[(i+1)+j for j in range(5)] for i in range(4)]

print_arr(a)
print_arr(b)

c = product(a, b)
print_arr(c)





