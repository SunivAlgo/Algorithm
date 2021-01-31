<h1>h-index</h1>

#### 0. 코드
```
def solution(citations):
    cnt = 0
    citations.sort(reverse= True)
    for i in range(len(citations)):
        if i + 1 != len(citations):
            if citations[i] <= cnt and citations[i + 1] <= cnt:
                break
        else:
            if citations[i] <= cnt:
                break
        cnt += 1
    return cnt
```
#### 1. 접근
내림차순으로 정렬하면 쉽게 풀릴거 같은 생각이 바로 들어서 비교적 쉽게 풀 수 있었다.
#### 2. 구현
* 초기 생각했던 구현 순서
우선 배열을 정렬을 하고 한 원소씩 돌아가면서 해당 원소의 차례에 조건이 맞다면 해당 카운트값을 반환하면 되지 않을까 생각했다. 비교적 쉽게 풀었기 때문에 넘어 가겠다.
#### 3. 배웠던 부분
.sort(reverse = True) 를 쓰면 순서가 반대로 정렬된다.

