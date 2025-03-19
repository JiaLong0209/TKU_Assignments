
def quick_sort(arr):
    if len(arr) < 2: return arr

    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    result = [*quick_sort(left), pivot, *quick_sort(right)]

    print(f'  | left: {left}, pivot: {pivot}, right: {right}')
    print(f'  | result: {result}')
    print('-------')

    return result

def partition_lomuto(arr, low, high):
    n = len(arr)
    pivot = arr[high]
    next_index = low
    for i in range(low, n-1):
        if arr[i] < pivot:
            arr[next_index], arr[i] = arr[i], arr[next_index]
            next_index += 1
    print(f'  low: {low}, high: {high}, part_index: {next_index}, pivot: {pivot}')
    print(f'  {arr}')
    print(f'-----------')
    arr[next_index], arr[high] = arr[high], arr[next_index]
    return next_index

def partition_hoare(arr, start, end):
    global total_nk 
    pivot = arr[start]
    left_index = start+1
    right_index = end
    done = False
    while not done:
        while left_index <= right_index and arr[left_index] <= pivot:
            total_nk += 1
            print(f'  Left: {left_index}, comparison_times: {total_nk}')
            left_index += 1

        while right_index >= left_index and arr[right_index] >= pivot:
            total_nk += 1
            print(f'  Right: {right_index}, comparison_times: {total_nk}')
            right_index -= 1

        if right_index < left_index:
            done = True
        else: 
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
            print(f'  Swap (left, right): left = {arr[left_index]} ({left_index}), right = {arr[right_index]} ({right_index})')
            print(f'  {arr}\n')

    arr[start], arr[right_index] = arr[right_index], arr[start]
    print(f'  Swap (start, right): start = {arr[start]} ({start}), right = {arr[right_index]} ({right_index})')
    print(f'  {arr}')
    print('---------')
    return right_index

def quick_sort_lomuto(arr, start, end):
    if(start < end):
        pivot_index = partition_hoare(arr, start, end)
        quick_sort_lomuto(arr, start, pivot_index-1)
        quick_sort_lomuto(arr, pivot_index+1, end)
    return arr


def main():
    arr = [15, 22, 13, 27, 12, 10, 20, 25]
    global total_nk
    total_nk = 0

    print(arr)
    # sorted_arr = quick_sort(arr)
    # print(sorted_arr)

    n = len(arr)
    quick_sort_lomuto(arr, 0, n-1)
    print(f'sorted_arr: {arr}')
    print(f'Total comparison times: {total_nk}')

    
main()

