# 단어 변환

###### 문제 설명

두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

```
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
```

예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 각 단어는 알파벳 소문자로만 이루어져 있습니다.
- 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
- words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
- begin과 target은 같지 않습니다.
- 변환할 수 없는 경우에는 0를 return 합니다.

##### 입출력 예

| begin | target | words                                      | return |
| ----- | ------ | ------------------------------------------ | ------ |
| "hit" | "cog"  | ["hot", "dot", "dog", "lot", "log", "cog"] | 4      |
| "hit" | "cog"  | ["hot", "dot", "dog", "lot", "log"]        | 0      |

##### 입출력 예 설명

예제 #1
문제에 나온 예와 같습니다.

예제 #2
target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다.



### Code

```python
from collections import deque

def search(begin,target,words,alphaSet):
    q = deque()
    visit = {word:0 for word in words}
    visit[begin] = 1
    q.append(begin)
    while q:
        nowNode = q.popleft()
        if nowNode == target:
            # print(visit)
            return visit[nowNode]-1
        for i,now in enumerate(nowNode):
            for ch in alphaSet[i]:
                if ch == now:
                    continue
                newWord = nowNode[:i]+ch+nowNode[i+1:]
                if newWord in words and not visit[newWord]:
                    visit[newWord] = visit[nowNode]+1
                    q.append(newWord)
    return 0
def solution(begin,target,words):
    # init
    alphaSet ={i:set() for i,_ in enumerate(begin)}
    for word in words:
        for i,w in enumerate(word):
            alphaSet[i].add(w)
    # pprint(alphaSet)
    return search(begin,target,words,alphaSet)
        



print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", ["1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)
```

### Solution

BFS 문제 `+1`

상당히 비효율적으로 푼 것 같다.

우선 나는 alphaSet 을 만들어주었다. alphaSet은 각 TestCase마다 다음과 같이 구성되어있따.

```python
{0: {'l', 'd', 'h', 'c'}, 1: {'o'}, 2: {'t', 'g'}}

{0: {'l', 'd', 'h'}, 1: {'o'}, 2: {'t', 'g'}}

{0: {'l', 'd', 'h'}, 1: {'o'}, 2: {'t', 'g'}}

{0: {'1'},
 1: {'2'},
 2: {'3'},
 3: {'4'},
 4: {'5'},
 5: {'6'},
 6: {'7'},
 7: {'8'},
 8: {'0', '9'},
 9: {'0', '9'}}

{0: {'l', 'd', 'h', 'c'}, 1: {'o'}, 2: {'t', 'g'}}
```

각 자리수마다 있는 글자들이 Set 으로 구성된 변수다.

그 후 만들어지는 새로운 word에 대해서 words안에 있는지 검사하고,  `visit`을 체크해주었고 queue에 넣었다.

만약 현재의 노드가 Target과 같다면 `visit[nowNode]-1` 로 리턴한다

> -1을 해주는 이유는 첫 시작을 1로 했기 때문



다른 사람 풀이 중 generator를 쓴 사람의 풀이를 보았다.

```python
from collections import deque
def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)
```

해당 코드는 `yield`를 for문 속에서 사용해서 만들어지는 word를 return값으로 전달하고 계속 for문을 돌게하여 확인하였다.