# 숫자의 표현

[출처 - Programmers](https://programmers.co.kr/learn/courses/30/lessons/12924)

###### 문제 설명

Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

- 1 + 2 + 3 + 4 + 5 = 15
- 4 + 5 + 6 = 15
- 7 + 8 = 15
- 15 = 15

자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

##### 제한사항

- n은 10,000 이하의 자연수 입니다.

------

##### 입출력 예

| n    | result |
| ---- | ------ |
| 15   | 4      |

##### 입출력 예 설명

입출력 예#1
문제의 예시와 같습니다.



### Code

```python
from collections import deque
def solution(n):
    nlist = deque([x for x in range(1,n+1)])
    q = deque()
    sums = 0
    ans = 0
    while nlist:
        if sums > n:
            popValue = q.popleft()
            sums -= popValue
        elif sums < n:
            popValue = nlist.popleft()
            sums += popValue
            q.append(popValue)
        elif sums == n:
            ans+=1
            if nlist:
                popValue = nlist.popleft()
                q.append(popValue)
                sums+=popValue
    return ans+1
```

### Solution

Deque로 문제를 해결하였다. 처음에는 투포인터를 써야하는가 싶었는데, 굳이 그렇게 어렵게 풀 필요는 없었다.

sum이 n보다 크면 deque에서 Pop 하고, sum이 n보다 작으면 deque에 append 하고, 같으면 count 를 1 증가시키고 nlist가 비어있지 않으면 deque에 append 하면 끝

> 마지막에 ans+1 을 해준 이유는 n 자신에 대해서 카운트하지 않아서 +1을 해주었다.