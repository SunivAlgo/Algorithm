# 소수만들기

[출처 - Programmers](https://programmers.co.kr/learn/courses/30/lessons/12977)

###### 문제 설명

주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

##### 제한사항

- nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
- nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

------

##### 입출력 예

| nums        | result |
| ----------- | ------ |
| [1,2,3,4]   | 1      |
| [1,2,7,6,4] | 4      |

##### 입출력 예 설명

입출력 예 #1
[1,2,4]를 이용해서 7을 만들 수 있습니다.

입출력 예 #2
[1,2,4]를 이용해서 7을 만들 수 있습니다.
[1,4,6]을 이용해서 11을 만들 수 있습니다.
[2,4,7]을 이용해서 13을 만들 수 있습니다.
[4,6,7]을 이용해서 17을 만들 수 있습니다.



### Code

```python
from itertools import combinations
from math import sqrt,ceil
def primes(n):
    primes = [True if i != 1 else False for i in range(n+1)]
    primes[0] = False
    primes[1] = False
    sq = ceil(sqrt(n))
    for i in range(2,sq+1):
        if primes[i]:
            for j in range(i+i,n+1,i):
                if not primes[j]:
                    continue
                primes[j] = False
    # print(primes)
    return primes
def solution(nums):
    nums.sort()
    pri = primes(sum(nums[-3:]))
    count = 0
    # print(pri)
    for x in combinations(nums,3):
        if pri[sum(x)]:
        #    print(x)
           count+=1
    return count
```

### Solution

우선 Sort 후 맨 끝 3개를 더한 값이 가장 큰 값이므로 그 값에 대해 에라토스테네스의 체를 만들어 combination으로 3개씩 뽑아서 합한 값을 에라토스테네스의 체에 True 값으로 되어있으면 count+1 해준다.



`+2`