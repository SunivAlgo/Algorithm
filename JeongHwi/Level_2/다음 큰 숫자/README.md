# 다음 큰 숫자

[참조 - Programmers](https://programmers.co.kr/learn/courses/30/lessons/12911)

###### 문제 설명

자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

- 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
- 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
- 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

##### 제한 사항

- n은 1,000,000 이하의 자연수 입니다.

------

##### 입출력 예

| n    | result |
| ---- | ------ |
| 78   | 83     |
| 15   | 23     |

##### 입출력 예 설명

입출력 예#1
문제 예시와 같습니다.
입출력 예#2
15(1111)의 다음 큰 숫자는 23(10111)입니다.

### Code

```python
from collections import Counter
def solution(n):
    number = n
    nbin = list(bin(number)[2:])
    nCount = Counter(nbin)
    while True:
        number+=1
        new_bin = list(bin(number)[2:])
        newCount = Counter(new_bin)
        if nCount["1"] == newCount["1"]:
            break
    return number
```

### Solution

쉬운 문제

`bin` 함수는 2진수로 바꿔준다. 1씩 늘려가며 Count를 세서 1의 갯수만 체크해준다.



`+1`



