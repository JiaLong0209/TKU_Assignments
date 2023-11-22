def linear_regression(x, y):
    print(x)
    print(y)
    
    return [x*y for x,y in zip(x, y)]

# Seniority
x = [1,2,3,3.5,4,4.5,6,6,7]
# Salary
y = [30000,25000,35000,32000,35000,32000,35000,50000,40000] 

line = linear_regression(x, y)

print(line)
