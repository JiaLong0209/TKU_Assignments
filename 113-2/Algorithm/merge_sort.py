

def merge(left, right):
    result = []
    nk = 0

    print(f'  | left: {left} right: {right}')
    while len(left) and len(right):
        if(left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        nk += 1

    result = result+left if len(left) else result+right
    print(f'  | merged: {result}')

    global total_nk
    total_nk += nk

    print(f'  | total_nk: {total_nk} (+{nk})')
    return result

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid] # 0 ~ mid-1
    right = arr[mid:]

    merged = merge(merge_sort(left), merge_sort(right))
    print(f'------')
    return merged

# def merge(arr, left, mid, right):
#
# def merge_sort2(arr, left, right):

def main():
    arr = [27, 10 ,12, 20 , 25, 13, 15, 22]
    global total_nk
    total_nk = 0

    print(arr)
    sorted_arr = merge_sort(arr)
    # sorted_arr = merge_sort2(arr)
    print(sorted_arr)
    print(f'total_nk: {total_nk}')
    
main()









