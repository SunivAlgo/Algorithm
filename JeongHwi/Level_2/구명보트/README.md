# 구명보트

###### 문제 설명

무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 **2명**씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
- 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

##### 입출력 예

| people           | limit | return |
| ---------------- | ----- | ------ |
| [70, 50, 80, 50] | 100   | 3      |
| [70, 80, 50]     | 100   | 3      |



### Code

```python
from collections import deque
def solution(people,limit):
    people.sort(reverse=True)
    people = deque(people)
    boat = 0
    while people:
        if people[0] < limit//2:
            people.popleft()
            if people:
                people.pop()
            boat+=1
            continue
        if people[0] + people[-1] > limit:
            people.popleft()
            boat += 1
        elif people[0] + people[-1] <= limit:
            people.popleft()
            if people:
                people.pop()
            boat+=1
    return boat
```

### Solution

`people`을 역순으로 `sort`를 수행, 그리고 `people`을 `deque`로 만들어준다.

맨 처음과 맨 끝을 더했을 때 Limit 보다 크면 맨 처음 ([0] 번째 원소) 만 `pop`한다. 

> Boat에는 두 사람만 들어갈 수 있으므로..

맨 처음 (가장 큰 수) 와 맨 끝 (가장 작은 수) 를 더했음 에도 불구하고 limit을 넘어버리니까

가장 무거운 사람은 같이 탈 수 없다는 것이다. 그래서 가장 무거운 사람은 혼자 타야되므로 popleft만 시킨다.

만약 가장 무거운 사람과 가벼운 사람이 limit 을 넘지 않는다면 둘 다 같이 태워서 보낸다.

가장 무거운 사람이 limit 의 반보다 안 넘는다면 무조건 2명이 같이 탈 수 있으므로 계속 2명을 태워 내보낸다.

`if people`을 해주는 이유는 만약 `popleft`를 한 경우에 사람이 없으면 더 이상 `pop`을 할 수 없기 때문에 조건을 걸어 주어야 한다.



Longest TC : 4 (`13.38 ms `)

`+6`



