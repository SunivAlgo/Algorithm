# JadenCase 문자열 만들기

이번 주는 아침 9시~저녁 10시까지 학교에 있어서 제정신이 아니므로 설명이 불친절 할 수 있음

### Code

```python
def solution(s):
    answer = ''
    for idx, i in enumerate(s): 
        if (idx == 0): answer = i.upper()
        elif s[idx-1] == ' ': answer = ''.join([answer, i.upper()])
        else: answer = ''.join([answer, i.lower()])
    return answer
```

* 답을 보고 해결했는데 이게 왜 내 코드랑 틀린지 모르겠음

> 내코드 

```python
def solution(s):
    s = list(s)
    for i in range(len(s)):
        if i == 0:
            if s[i] == " ":
                continue
            if "a"<=s[i]<="z":
                s[i] = s[i].upper()
                continue
        if s[i-1] == " ":
            if "a"<=s[i]<="z":
                s[i] = s[i].upper()
        else:
            if "A"<=s[i]<="Z":
                s[i] = s[i].lower()
    return "".join(s)
```

### 좋은 Solution

#### `str.capitalize()`

* 첫 글자만 대문자로 만들어주는 함수

```python
>>> A = "aBCDefg"
>>> A.capitalize()
"Abcdefg"
```

