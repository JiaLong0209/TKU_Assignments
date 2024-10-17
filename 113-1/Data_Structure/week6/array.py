from functools import reduce

def print_arr(a, title = ""):
    print(f"\n{title}")
    for row in a:
        print(*row)

def addition(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]  for i in range(len(a))]

def product(a, b):
    return [[a[i][j] * b[i][j] for j in range(len(a[0]))]  for i in range(len(a))]

def dot(a, b):
    return [[ reduce(lambda acc, cur:acc+cur, [a[i][k] * b[k][j] for k in range(len(a[0]))])  for j in range(len(b[0]))] for i in range(len(a))]

def transpose(a):
    return [[a[j][i] for j in range(len(a)) ] for i in range(len(a[0]))]

def dot_test():
    print("----------------")
    print("Dot Test: ")
    # 3x4
    # a = [[(i+1)*(j+1) for j in range(4)] for i in range(3)]
    # 4x3
    # b = [[(i+1)-j for j in range(5)] for i in range(4)]

    # 2x3
    a = [[1,3,5], [7,9,11]]
    # 3x4
    b = [[2,4,6,8], [1,3,5,7], [0,1,2,3]]

    print_arr(a, "A:")
    print_arr(b, "B:")

    print_arr(dot(a,b), "A dot B:")

def addition_test():
    # 3x3 
    print("----------------")
    print("Addition Test: ")
    c = [[(i+1)*(j+1) for j in range(3)] for i in range(3)]
    # 3x3 
    d = [[(i+1)+(j+1) for j in range(3)] for i in range(3)]

    print_arr(c, "C:")
    print_arr(d, "D:")
    print_arr(addition(c,d) , "C+D:")

def product_test():
    print("----------------")
    print("Product Test: ")
    # 3x3 
    c = [[(i+1)*(j+1) for j in range(3)] for i in range(3)]
    # 3x3 
    d = [[(i+1)+(j+1) for j in range(3)] for i in range(3)]

    print_arr(c, "C:")
    print_arr(d, "D:")
    print_arr(product(c,d) , "C*D:")

def transpose_test():
    print("----------------")
    print("Transpose Test: ")
    # 3 x 4
    a = [[2,4,6,8], [1,3,5,7], [0,1,2,3]]
    print_arr(a, "A:")
    print_arr(transpose(a) , "A':")


dot_test()
addition_test()
product_test()

transpose_test()

