import math
n = 1000000
prime = [2]
count = 0
answer = 0
for i in range (3, n+1):
    for j in prime:
        if i % j == 0:
            count += 1
            break
        if j > math.sqrt(i):
            break
    if count == 0:
        prime.append(i)
    count = 0
answer = len(prime)
print(answer)


