from itertools import accumulate
from functools import reduce

def calc_scores():
    scores = [50, 60, 20, 50, 90]
    for i, score in enumerate(scores):
        print(f'{i}: {score}')
    total_score = reduce(lambda a, b: a+b, scores)
    print(f"total score: {total_score}")
    print(list(accumulate(scores, lambda a,b: a+b)))

def array_address_diff_2d(arr):
    s = id(arr[0][0])
    e = id(arr[len(arr)-1][len(arr[0])-1])
    return e-s


# calc_scores()

arr = [[(10*i)+j for j in range(0,10)] for i in range(0, 10)]
print(array_address_diff_2d(arr))

# print(0x1000)
# print(hex(0x1000 + 0x4 * 500))

