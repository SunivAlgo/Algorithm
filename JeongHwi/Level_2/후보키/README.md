# 후보키

[출처 - Programmers](https://programmers.co.kr/learn/courses/30/lessons/42890)

###### 문제 설명

프렌즈대학교 컴퓨터공학과 조교인 제이지는 네오 학과장님의 지시로, 학생들의 인적사항을 정리하는 업무를 담당하게 되었다.

그의 학부 시절 프로그래밍 경험을 되살려, 모든 인적사항을 데이터베이스에 넣기로 하였고, 이를 위해 정리를 하던 중에 후보키(Candidate Key)에 대한 고민이 필요하게 되었다.

후보키에 대한 내용이 잘 기억나지 않던 제이지는, 정확한 내용을 파악하기 위해 데이터베이스 관련 서적을 확인하여 아래와 같은 내용을 확인하였다.

- 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
  - 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
  - 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

제이지를 위해, 아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.

![cand_key1.png](https://grepp-programmers.s3.amazonaws.com/files/production/f1a3a40ede/005eb91e-58e5-4109-9567-deb5e94462e3.jpg)

위의 예를 설명하면, 학생의 인적사항 릴레이션에서 모든 학생은 각자 유일한 "학번"을 가지고 있다. 따라서 "학번"은 릴레이션의 후보 키가 될 수 있다.
그다음 "이름"에 대해서는 같은 이름("apeach")을 사용하는 학생이 있기 때문에, "이름"은 후보 키가 될 수 없다. 그러나, 만약 ["이름", "전공"]을 함께 사용한다면 릴레이션의 모든 튜플을 유일하게 식별 가능하므로 후보 키가 될 수 있게 된다.
물론 ["이름", "전공", "학년"]을 함께 사용해도 릴레이션의 모든 튜플을 유일하게 식별할 수 있지만, 최소성을 만족하지 못하기 때문에 후보 키가 될 수 없다.
따라서, 위의 학생 인적사항의 후보키는 "학번", ["이름", "전공"] 두 개가 된다.

릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때, 이 릴레이션에서 후보 키의 개수를 return 하도록 solution 함수를 완성하라.

##### 제한사항

- relation은 2차원 문자열 배열이다.
- relation의 컬럼(column)의 길이는 `1` 이상 `8` 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
- relation의 로우(row)의 길이는 `1` 이상 `20` 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
- relation의 모든 문자열의 길이는 `1` 이상 `8` 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다.
- relation의 모든 튜플은 유일하게 식별 가능하다.(즉, 중복되는 튜플은 없다.)

##### 입출력 예

| relation                                                     | result |
| ------------------------------------------------------------ | ------ |
| `[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]` | 2      |

##### 입출력 예 설명

입출력 예 #1
문제에 주어진 릴레이션과 같으며, 후보 키는 2개이다.



### Code

```python
from itertools import combinations
def getSubData(re_dict,keys):
    s = []
    for k in keys:
        s.append(re_dict[k])
    sub = []
    for i in range(len(s[0])):
        sub.append(tuple([x[i] for x in s]))
    return sub
        

def solution(relation):
    relen = len(relation)
    inlen = len(relation[0])
    re_dict = {}
    #initialize Dictionary
    for i in range(inlen):
        re_dict[i] = []
    for r in relation:
        for i in range(inlen):
            re_dict[i].append(r[i])
    
    # Get Unique
    unique = []
    for i in range(1,len(re_dict)+1):
        for x in combinations(re_dict.keys(),i):
            subData = getSubData(re_dict,x)
            if len(set(subData)) == relen:
                unique.append(x)
    # print(unique)

    # 최소성 (답을 봄)
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
```

### Solution

**답을 보고 해결함**

우선 각 row들을 dictionary로 통해 column으로 나눈 다음 모든 column의 수를 조합해서 조합들에 대한 Row를 추출

추출된 row에 대해 유일성을 검사한다. 유일성을 검사하는 방법은 기존에 갖고있던 원소들의 갯수를 set으로 처리했을 때 중복으로 인해 제거가 되면 원래 가져야할 원소들의 개수와 맞춰져야한다. (중복이 없으면 개수와 같다)

최소성은 유일성으로 검증된 후보키들가 다른 후보키들을 부분집합으로 가진다면 해당 후보키는 최소성을 만족하지 않는다.

```python
[(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

{(1, 2), (0,), (0, 1, 2), (0, 2, 3), (0, 1, 3), (1, 2, 3), (0, 3), (0, 2), (0, 1, 2, 3)}
{(1, 2), (0,), (0, 1, 2), (0, 2, 3), (0, 1, 3), (1, 2, 3), (0, 3), (0, 1, 2, 3)}
{(1, 2), (0,), (0, 1, 2), (0, 2, 3), (0, 1, 3), (1, 2, 3), (0, 1, 2, 3)}
{(1, 2), (0,), (0, 2, 3), (0, 1, 3), (1, 2, 3), (0, 1, 2, 3)}
{(1, 2), (0,), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)}
{(1, 2), (0,), (1, 2, 3), (0, 1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,), (1, 2, 3)}
{(1, 2), (0,)}
{(1, 2), (0,)}
{(1, 2), (0,)}
{(1, 2), (0,)}
{(1, 2), (0,)}
{(1, 2), (0,)}
```

해당 출력은 부분집합을 체크해서 제거되는 경우다.

(0,) 과 (0,1) 을 체크하는데, 0은 0,1의 부분집합이 되므로 0,1은 최소성을 만족하지 않게되고 삭제되는 경우가 된다.

그래서 최종적으로 [1,2] , [0] 만 남게되고 해당이 답이된다

--> 최소성이 어려웠음

`+5`