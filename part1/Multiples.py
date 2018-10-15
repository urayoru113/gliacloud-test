sum_ = 0
for i in range(0, 1001):
    if i%3 == 0:
        sum_ += i
    if i%5 == 0:
        sum_ += i
    if i%15 == 0:
        sum_ -= i

print(sum_)

# or another answer

def accumulate(n):
    return (n*(n+1))/2

a = 1000//3
b = 1000//5
c = 1000//15

print(3*accumulate(a) + 5*accumulate(b) - 15*accumulate(c))
