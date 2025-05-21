import numpy as np

def print_arr(arr, title = ''):
    print(title)
    for i in arr:
        for j in i:
            print(f"{j:<5}", end='')
        print()
    print()

def floyd(W, start, end):
    # D = np.zeros((len(W), len(W)))
    n = len(W)
    D = W
    P = [[0 for i in range(n)] for j in range(n)]

    print(f'v{start} -> v{end}: ')
    print_arr(D, "Distance: ")
    for k in range(n):
        print(f'k = {k}')

        
        for i in range(n):
            for j in range(n):
                if(D[i][k] + D[k][j] < D[i][j]):
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k
                    print(f'D[{i}][{j}] = {D[i][j]}')

        print_arr(D, "Distance: ")
        print_arr(P, "P throgh Vertices:")

def main():
    W = [
            [0, 1, 1000, 1, 5],
            [9, 0, 3, 2, 1000],
            [1000, 1000, 0, 4, 1000],
            [1000, 1000, 2, 0, 3],
            [3, 1000, 1000, 1000, 0],
        ]

    # num = (16%5) +1
    start = 2
    end = 5

    print("Flody: ")
    floyd(W, start, end)

if __name__ == "__main__":
    main()
