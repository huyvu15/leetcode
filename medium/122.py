a = [7,1,5,3,6,4]

b = [1,2,3,4,5]

c = [7,6,4,3,1]

def ok(a):
    # if not a.index(min(a)):
    #     return 0
    # min_pos = a.index(min(a))
    # sum_profit = 0
    # for i in range(min_pos, len(a)):
    #     sum_profit = min[i+1] - min(a)
    
    sum = 0
    for i in range(len(a)-1):
        if a[i + 1] > a[i]:
            sum += a[i + 1] - a[i]
    return sum

print(ok(b))   
    
print(a.index(min(a)))