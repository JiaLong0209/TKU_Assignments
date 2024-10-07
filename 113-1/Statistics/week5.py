import math

data = [2038, 1758, 1721, 1637, 2097, 2047, 2205, 1787, 2287, 1940, 2311, 2054, 2406, 1471, 1460]

data = sorted(data)
print(data)

def percentile_position(data, percent):
    return math.floor((len(data)) * (percent/100))

print(len(data))

print(f"First quartile: {data[percentile_position(data,25)]}")
print(f"Median: {data[percentile_position(data,50)]}")
print(f"Thrid quartile: {data[percentile_position(data,75)]}")


