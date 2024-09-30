import math
from functools import reduce

# 19+17+22+18+28+34+45+39+38+44+34+10
ex1 = [19,17,22,18,28,34,45,39,38,44,34,10]

# variance = ((19-29)^2+ (17-29)^2+ (22-29)^2+ (18-29)^2+ (28-29)^2+ (34-29)^2+ (45-29)^2+ (39-29)^2+ (38-29)^2+ (44-29)^2+ (34-29)^2+ (10-29)^2)/12

class Tool:
    def __init__(self, data = []):
        self.data = data

    def mean(self, data):
        return sum(data) / len(data)

    def range(self, data):
        return max(data) - min(data)

    def median(self, data):
        return data[math.floor(len(data)/2)] if len(data) % 2 else (data[math.floor(len(data)/2)] + data[math.floor(len(data)/2)-1]) / 2

    def variance(self, data):
        mean = self.mean(data)
        variance = sum([(x-mean)**2 for x in data]) / len(data)
        return variance

    def sample_variance(self, data):
        mean = self.mean(data)
        variance = sum([(x-mean)**2 for x in data]) / (len(data)-1)
        return variance
    
    def info(self, data = []):
        data = self.data if data == [] else data
        print('-'*30)
        print(data)
        print(f"Mean: {self.mean(data)}")
        print(f"Median: {self.median(data)}")
        print(f"Range: {self.range(data)}")
        print(f"Variance: {self.variance(data)}")
        print(f"Sample Variance: {self.sample_variance(data)}")
        print(f"Sample Variance Literal: {self.sample_variance_literal(data)}")

    def sample_variance_literal(self, data):
        str = ""
        str += "("
        for index, n in enumerate(data):
            str += "("
            str += f"{data[index]}-{self.mean(data)}"
            str += ")^2"
            if (index != len(data) - 1): 
                str += "+"
        str += f") / ({len(data)}-1)"
        
        return str

    def PR(self, data, target):
        data = sorted(data)
        # pr = (100/len(data) * len(list(filter(lambda a: a < target, data)))) + (100/len(data) * (1/2))

        l = list(filter(lambda a: a < target, data))
        won = len(l)
        print(l, won)
        
        pr = (100/len(data) * len(list(filter(lambda a: a < target, data)))) + (100/len(data) * (1/2))
        return pr

t = Tool()
ex2 = [12, 20, 16, 18, 19]
pr_ex = [90, 76, 83, 35 ,56, 71, 78, 84, 62 ,96]
# t.info()
# t.info(ex2)
print(t.PR(pr_ex, 84))

print(sorted(pr_ex))

