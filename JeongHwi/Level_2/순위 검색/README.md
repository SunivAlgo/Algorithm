# [순위 검색](https://programmers.co.kr/learn/courses/30/lessons/72412)(★) [2021 KAKAO BLINE RECRUITMENT]

###### 문제 설명

**[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]**

카카오는 하반기 경력 개발자 공개채용을 진행 중에 있으며 현재 지원서 접수와 코딩테스트가 종료되었습니다. 이번 채용에서 지원자는 지원서 작성 시 아래와 같이 4가지 항목을 반드시 선택하도록 하였습니다.

- 코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
- 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
- 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
- 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.

인재영입팀에 근무하고 있는 `니니즈`는 코딩테스트 결과를 분석하여 채용에 참여한 개발팀들에 제공하기 위해 지원자들의 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구를 만들고 있습니다.
예를 들어, 개발팀에서 궁금해하는 문의사항은 다음과 같은 형태가 될 수 있습니다.
`코딩테스트에 java로 참여했으며, backend 직군을 선택했고, junior 경력이면서, 소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 50점 이상 받은 지원자는 몇 명인가?`

물론 이 외에도 각 개발팀의 상황에 따라 아래와 같이 다양한 형태의 문의가 있을 수 있습니다.

- 코딩테스트에 python으로 참여했으며, frontend 직군을 선택했고, senior 경력이면서, 소울푸드로 chicken을 선택한 사람 중 코딩테스트 점수를 100점 이상 받은 사람은 모두 몇 명인가?
- 코딩테스트에 cpp로 참여했으며, senior 경력이면서, 소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 100점 이상 받은 사람은 모두 몇 명인가?
- backend 직군을 선택했고, senior 경력이면서 코딩테스트 점수를 200점 이상 받은 사람은 모두 몇 명인가?
- 소울푸드로 chicken을 선택한 사람 중 코딩테스트 점수를 250점 이상 받은 사람은 모두 몇 명인가?
- 코딩테스트 점수를 150점 이상 받은 사람은 모두 몇 명인가?

즉, 개발팀에서 궁금해하는 내용은 다음과 같은 형태를 갖습니다.

```
* [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
```

------

#### **[문제]**

지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info, 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

#### **[제한사항]**

- info 배열의 크기는 1 이상 50,000 이하입니다.

- info 배열 각 원소의 값은 지원자가 지원서에 입력한 4가지 값과 코딩테스트 점수를 합친

   

  개발언어 직군 경력 소울푸드 점수

   

  형식입니다.

  - 개발언어는 cpp, java, python 중 하나입니다.
  - 직군은 backend, frontend 중 하나입니다.
  - 경력은 junior, senior 중 하나입니다.
  - 소울푸드는 chicken, pizza 중 하나입니다.
  - 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.
  - 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.

- query 배열의 크기는 1 이상 100,000 이하입니다.

- query의 각 문자열은

   

  [조건] X

   

  형식입니다.

  - [조건]은 개발언어 and 직군 and 경력 and 소울푸드 형식의 문자열입니다.
  - 언어는 cpp, java, python, - 중 하나입니다.
  - 직군은 backend, frontend, - 중 하나입니다.
  - 경력은 junior, senior, - 중 하나입니다.
  - 소울푸드는 chicken, pizza, - 중 하나입니다.
  - '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
  - X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.
  - 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.
  - 예를 들면, cpp and - and senior and pizza 500은 cpp로 코딩테스트를 봤으며, 경력은 senior 이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 500점 이상 받은 사람은 모두 몇 명인가?를 의미합니다.

------

##### **[입출력 예]**

| info                                                         | query                                                        | result        |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------- |
| `["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]` | `["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]` | [1,1,1,1,2,4] |

##### **입출력 예에 대한 설명**

지원자 정보를 표로 나타내면 다음과 같습니다.

| 언어   | 직군     | 경력   | 소울 푸드 | 점수 |
| ------ | -------- | ------ | --------- | ---- |
| java   | backend  | junior | pizza     | 150  |
| python | frontend | senior | chicken   | 210  |
| python | frontend | senior | chicken   | 150  |
| cpp    | backend  | senior | pizza     | 260  |
| java   | backend  | junior | chicken   | 80   |
| python | backend  | senior | chicken   | 50   |

- `"java and backend and junior and pizza 100"` : java로 코딩테스트를 봤으며, backend 직군을 선택했고 junior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 100점 이상 받은 지원자는 1명 입니다.
- `"python and frontend and senior and chicken 200"` : python으로 코딩테스트를 봤으며, frontend 직군을 선택했고, senior 경력이면서 소울 푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 200점 이상 받은 지원자는 1명 입니다.
- `"cpp and - and senior and pizza 250"` : cpp로 코딩테스트를 봤으며, senior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 250점 이상 받은 지원자는 1명 입니다.
- `"- and backend and senior and - 150"` : backend 직군을 선택했고, senior 경력인 지원자 중 코딩테스트 점수를 150점 이상 받은 지원자는 1명 입니다.
- `"- and - and - and chicken 100"` : 소울푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 100점 이상을 받은 지원자는 2명 입니다.
- `"- and - and - and - 150"` : 코딩테스트 점수를 150점 이상 받은 지원자는 4명 입니다.



### Code

```python
from itertools import combinations
from bisect import bisect_left
infos = {}
def getinfos(score,info_):
    global infos
    for k in range(5):    
        for x in combinations([0,1,2,3],k):
            case = ""
            for i in range(4):
                if i not in x:
                    case += info_[i]
                else:
                    case += "-"
            if case not in infos:
                infos[case]=[int(score)]
            else:
                infos[case].append(int(score))

def solution(info,query):
    for i in info:
        info_split = i.split()
        score = info_split[-1]
        info_ = info_split[:-1]
        getinfos(score,info_)
    for x in infos.keys():
        infos[x].sort()
    ans = []
    for q in query:
        q = q.replace("and","")
        q_split = q.split()
        condition = "".join(q_split[:4])
        score = int(q_split[4])
        if condition in infos:
            ans.append(len(infos[condition])-bisect_left(infos[condition],score,lo=0,hi=len(infos[condition])))
        else:
            ans.append(0)
    return ans

# 시간초과 코드
"""
from collections import Counter
def condition_Check(conditions,applicants):
    sub_ans = []
    notCondition = 0
    for i,cond in enumerate(["language","job","career","soulFood"]):
        if conditions[i] == "-":
            for x in applicants[cond]:
                sub_ans += applicants[cond][x]
            continue
        sub_ans += applicants[cond][conditions[i]]
    counter = [x for x,c in Counter(sub_ans).items() if c == 4]
    # print(counter)
    count = 0
    for i in counter:
        if int(applicants["score"][i]) >= int(conditions[4]):
            count+=1
    return count
def solution(info,query):
    # init
    applicants = {"language":{"java":[],"cpp":[],"python":[]},
                  "job":{"backend":[],"frontend":[]},
                  "career":{"junior":[],"senior":[]},
                  "soulFood":{"chicken":[],"pizza":[]},
                  "score":{}}
    for number,info_ in enumerate(info):
        infos = info_.split()
        applicants["language"][infos[0]].append(number)
        applicants["job"][infos[1]].append(number)
        applicants["career"][infos[2]].append(number)
        applicants["soulFood"][infos[3]].append(number)
        applicants["score"][number] = infos[4]
    # pprint.pprint(applicants)
    ans = []
    # query
    for q in query:
        query_Split = q.split()
        conditions = [query_Split[0],query_Split[2],query_Split[4],query_Split[6],query_Split[7]]    
        ans.append(condition_Check(conditions,applicants))
    return ans
"""
```

### Solution

[정답](https://velog.io/@djagmlrhks3/Algorithm-Programmers-%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89-by-Python)을 보고 해결하였습니다.

해설은 위 블로그를 참고하시길 바랍니다.



나는 처음에 멀티 딕셔너리를 하고 list를 extend 하는 방향으로 했는데 시간이 더 오래걸렸다. (효율성에서 0점)

아무래도 `"-"` 조건이 들어오면 들어올수록 탐색해야하는 수가 급증해서 처리하는 시간이 오래걸리게 된 것 같다.

또한 `Counter` 를 쓰는 것 조차 O(N) 만큼 걸려버리니까 그만큼 시간을 더 잡아 먹는다.

`맞는 코드`에서는 전체 경우의 수에서만 스코어를 탐색하면 되는데, 내 `시간초과 코드`는 모든 사람의 수 * N(`"-"` 인 경우) 만큼 체크를 해야하므로 시간이 더욱 걸렸다..

그리고 여기서

`bisect` 라이브러리를 배웠다. 

`bisect`는 이분탐색 라이브러리로, `bisect_left(a,x,lo,hi)` 인 경우에 a배열에 x가 위치해야할 곳이 어딘지 이분탐색으로 찾는다.

따라서 위 코드에서는 `한 경우의 수의 value 배열길이 `- `이분탐색으로 x가 위치해야할 곳` 을 해주면 x보다 이상인 값의 갯수가 나오게 된다. 



적어도 이 문제는 Level2 난이도는 아닌 것 같다.

그리고 카카오 문제는 정말 어렵다..