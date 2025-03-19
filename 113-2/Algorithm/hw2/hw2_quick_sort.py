
def partition_hoare(arr, start, end):
    global total_nk 
    pivot = arr[start]
    left_index = start+1
    right_index = end
    done = False
    print(f'  Pivot: {pivot}, Left: {arr[left_index]} ({left_index}), Right: {arr[right_index]} ({right_index})')
    while not done:
        while left_index <= right_index and arr[left_index] <= pivot:
            total_nk += 1
            print(f'  --Left: {arr[left_index]} ({left_index}), count: {total_nk}')
            left_index += 1

        while right_index >= left_index and arr[right_index] >= pivot:
            total_nk += 1
            print(f'  --Right: {arr[right_index]} ({right_index}), count: {total_nk}')
            right_index -= 1

        if right_index < left_index:
            done = True
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


# output:
# [15, 22, 13, 27, 12, 10, 20, 25]
#   Pivot: 15
#   Right: 25 (7), comparison_times: 1
#   Right: 20 (6), comparison_times: 2
#   Left: 22 (1), Right: 10 (5)
#   Swap (left, right): left = 10 (1), right = 22 (5)
#   [15, 10, 13, 27, 12, 22, 20, 25]
#
#   Left: 10 (1), comparison_times: 3
#   Left: 13 (2), comparison_times: 4
#   Right: 22 (5), comparison_times: 5
#   Left: 27 (3), Right: 12 (4)
#   Swap (left, right): left = 12 (3), right = 27 (4)
#   [15, 10, 13, 12, 27, 22, 20, 25]
#
#   Left: 12 (3), comparison_times: 6
#   Right: 27 (4), comparison_times: 7
#   Swap (start, right): start = 12 (0), right = 15 (3)
#   [12, 10, 13, 15, 27, 22, 20, 25]
# ---------
#   Pivot: 12
#   Left: 10 (1), comparison_times: 8
#   Right: 13 (2), comparison_times: 9
#   Swap (start, right): start = 10 (0), right = 12 (1)
#   [10, 12, 13, 15, 27, 22, 20, 25]
# ---------
#   Pivot: 27
#   Left: 22 (5), comparison_times: 10
#   Left: 20 (6), comparison_times: 11
#   Left: 25 (7), comparison_times: 12
#   Swap (start, right): start = 25 (4), right = 27 (7)
#   [10, 12, 13, 15, 25, 22, 20, 27]
# ---------
#   Pivot: 25
#   Left: 22 (5), comparison_times: 13
#   Left: 20 (6), comparison_times: 14
#   Swap (start, right): start = 20 (4), right = 25 (6)
#   [10, 12, 13, 15, 20, 22, 25, 27]
# ---------
#   Pivot: 20
#   Right: 22 (5), comparison_times: 15
#   Swap (start, right): start = 20 (4), right = 20 (4)
#   [10, 12, 13, 15, 20, 22, 25, 27]
# ---------
# sorted_arr: [10, 12, 13, 15, 20, 22, 25, 27]
# Total comparison times: 15
#
