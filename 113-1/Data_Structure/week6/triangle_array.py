
def print_arr(a, title = ""):
    print(f"\n{title}")
    for row in a:
        print(*row)


def compress_upper_triangle(arr, is_row_major = True):
    result = []
    if is_row_major:
        for i in range(len(arr)):
            for j in range(i, len(arr[0])):
                result.append(arr[i][j])
    else:
        for i in range(len(arr)):
            for j in range(i+1):
                result.append(arr[j][i])

    return result


def compress_upper_triangle_test():
    tri_arr = [[1,2,3,4],[0,5,6,7],[0,0,8,9],[0,0,0,10]]
    print_arr(tri_arr)
    compress_arr = compress_upper_triangle(tri_arr, False)
    print(compress_arr)

compress_upper_triangle_test()
