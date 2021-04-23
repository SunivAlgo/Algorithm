# 가장 긴 펠린드롬

###### 문제 설명

앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

예를들면, 문자열 s가 "abcdcba"이면 7을 return하고 "abacde"이면 3을 return합니다.

##### 제한사항

- 문자열 s의 길이 : 2,500 이하의 자연수
- 문자열 s는 알파벳 소문자로만 구성

------

##### 입출력 예

| s         | answer |
| --------- | ------ |
| "abcdcba" | 7      |
| "abacde"  | 3      |

##### 입출력 예 설명

입출력 예 #1
4번째자리 'd'를 기준으로 문자열 s 전체가 팰린드롬이 되므로 7을 return합니다.

입출력 예 #2
2번째자리 'b'를 기준으로 "aba"가 팰린드롬이 되므로 3을 return합니다.



### Code

```python
def solution(s):
    # 펠린드롬은 1도 있음
    """
    효율성 안따지고 구현
    """
    maxAns = -1
    slen = len(s)
    for i in range(slen):
        for j in range(i+1,slen):
            target = s[i:j+1]
            rTarget = target[::-1]
            if target == rTarget:
                # print(target, rTarget)
                maxAns = max(maxAns, j-i+1)
                # print(maxAns)
    if maxAns == -1:
        return 1
    return maxAns
print(solution("abcdcba"),7)
print(solution("abacde"),3)
```



### Solution

`+7`

단순하게 완전탐색 방식으로 구현했다.

이중 폴문으로 구현하였는데

`abcdcba`를 예시로 들어보면 출력은 다음과 같다.

```python
#print(s[i:j+1])
ab
abc
abcd
abcdc
abcdcb
abcdcba
bc
bcd
bcdc
bcdcba
cd
...
```

여기서 문자열 자체를 reverse 시킨 `target[::-1]` 과 `target`이 동일하다면

max 값을 업데이트 시켜준다.