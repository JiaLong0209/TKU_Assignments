
def partition_hoare(arr, start, end):
    global total_nk 
    pivot = arr[start]
    left_index = start+1
    right_index = end
    print(f'  Pivot: {pivot}, Left: {arr[left_index]} ({left_index}), Right: {arr[right_index]} ({right_index})')

    while left_index <= right_index:
        while left_index <= right_index and arr[left_index] <= pivot:
            total_nk += 1
            print(f'  --Left: {arr[left_index]} ({left_index}), count: {total_nk}')
            left_index += 1

        while right_index >= left_index and arr[right_index] >= pivot:
            total_nk += 1
            print(f'  --Right: {arr[right_index]} ({right_index}), count: {total_nk}')
            right_index -= 1

        if right_index < left_index:
            break
        else: 
            print(f'  --Left: {arr[left_index]} ({left_index}), Right: {arr[right_index]} ({right_index})')
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
            print(f'  Swap (left, right): left = {arr[left_index]} ({left_index}), right = {arr[right_index]} ({right_index})')
            print(f'  {arr}\n')

    arr[start], arr[right_index] = arr[right_index], arr[start]
    print(f'  Swap (start, right): start = {arr[start]} ({start}), right = {arr[right_index]} ({right_index})')
    print(f'  L: {arr[:right_index]}, P: [{pivot}], R: {arr[right_index+1 :]}')
    print(f'  {arr}')
    print('---------')
    return right_index

def quick_sort(arr, start, end):
    if(start < end):
        pivot_index = partition_hoare(arr, start, end)
        quick_sort(arr, start, pivot_index-1)
        quick_sort(arr, pivot_index+1, end)
    return arr

def main():
    num = 16
    arr = [15, 22, 13, 27, num, 12, 10, 20, 25]
    global total_nk
    total_nk = 0
    print(arr)
    n = len(arr)
    quick_sort(arr, 0, n-1)
    print(f'sorted_arr: {arr}')
    print(f'Total comparison times: {total_nk}')
main()


# 15, 22, 13, 27, 16, 12, 10, 20, 25
# 13, 12, 10, |15|, 16, 22, 27, 20, 25
# 12, 10, |13|, |15|, 16, 22, 27, 20, 25
# 10, |12|, |13|, |15|, 16, 22, 27, 20, 25
# |10|, |12|, |13|, |15|, 16, 22, 27, 20, 25
# |10|, |12|, |13|, |15|, |16|, 22, 27, 20, 25
# |10|, |12|, |13|, |15|, |16|, 20, |22|, 27, 25
# |10|, |12|, |13|, |15|, |16|, |20|, |22|, 27, 25
# |10|, |12|, |13|, |15|, |16|, |20|, |22|, 25, |27|
# |10|, |12|, |13|, |15|, |16|, |20|, |22|, |25|, |27|




# output:

# [15, 22, 13, 27, 16, 12, 10, 20, 25]
#   Pivot: 15, Left: 22 (1), Right: 25 (8)
#   --Right: 25 (8), count: 1
#   --Right: 20 (7), count: 2
#   --Left: 22 (1), Right: 10 (6)
#   Swap (left, right): left = 10 (1), right = 22 (6)
#   [15, 10, 13, 27, 16, 12, 22, 20, 25]
#
#   --Left: 10 (1), count: 3
#   --Left: 13 (2), count: 4
#   --Right: 22 (6), count: 5
#   --Left: 27 (3), Right: 12 (5)
#   Swap (left, right): left = 12 (3), right = 27 (5)
#   [15, 10, 13, 12, 16, 27, 22, 20, 25]
#
#   --Left: 12 (3), count: 6
#   --Right: 27 (5), count: 7
#   --Right: 16 (4), count: 8
#   Swap (start, right): start = 12 (0), right = 15 (3)
#   L: [12, 10, 13], P: [15], R: [16, 27, 22, 20, 25]
#   [12, 10, 13, 15, 16, 27, 22, 20, 25]
# ---------
#   Pivot: 12, Left: 10 (1), Right: 13 (2)
#   --Left: 10 (1), count: 9
#   --Right: 13 (2), count: 10
#   Swap (start, right): start = 10 (0), right = 12 (1)
#   L: [10], P: [12], R: [13, 15, 16, 27, 22, 20, 25]
#   [10, 12, 13, 15, 16, 27, 22, 20, 25]
# ---------
#   Pivot: 16, Left: 27 (5), Right: 25 (8)
#   --Right: 25 (8), count: 11
#   --Right: 20 (7), count: 12
#   --Right: 22 (6), count: 13
#   --Right: 27 (5), count: 14
#   Swap (start, right): start = 16 (4), right = 16 (4)
#   L: [10, 12, 13, 15], P: [16], R: [27, 22, 20, 25]
#   [10, 12, 13, 15, 16, 27, 22, 20, 25]
# ---------
#   Pivot: 27, Left: 22 (6), Right: 25 (8)
#   --Left: 22 (6), count: 15
#   --Left: 20 (7), count: 16
#   --Left: 25 (8), count: 17
#   Swap (start, right): start = 25 (5), right = 27 (8)
#   L: [10, 12, 13, 15, 16, 25, 22, 20], P: [27], R: []
#   [10, 12, 13, 15, 16, 25, 22, 20, 27]
# ---------
#   Pivot: 25, Left: 22 (6), Right: 20 (7)
#   --Left: 22 (6), count: 18
#   --Left: 20 (7), count: 19
#   Swap (start, right): start = 20 (5), right = 25 (7)
#   L: [10, 12, 13, 15, 16, 20, 22], P: [25], R: [27]
#   [10, 12, 13, 15, 16, 20, 22, 25, 27]
# ---------
#   Pivot: 20, Left: 22 (6), Right: 22 (6)
#   --Right: 22 (6), count: 20
#   Swap (start, right): start = 20 (5), right = 20 (5)
#   L: [10, 12, 13, 15, 16], P: [20], R: [22, 25, 27]
#   [10, 12, 13, 15, 16, 20, 22, 25, 27]
# ---------
# sorted_arr: [10, 12, 13, 15, 16, 20, 22, 25, 27]
# Total comparison times: 20
