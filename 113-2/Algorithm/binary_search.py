
def binary_search(l, x):
    print(f"=======================")
    low = 0
    high = len(l) - 1
    while(low <= high):
        mid = int((low + high)/2)
        print(f"low = {low:>3}\t mid = {mid:>3}\t high = {high:>3}")
        if(l[mid] == x):
            return mid+1
        elif(l[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return 0

def run_binary_search():
    l = [i for i in range(1, 101)]
    x = 16
    location = binary_search(l, x)
    print(f"=======================")
    if(location):
        print(f"Found {x} at location {location}")
    else:
        print(f"Not Found {x} in {l}")

run_binary_search()

