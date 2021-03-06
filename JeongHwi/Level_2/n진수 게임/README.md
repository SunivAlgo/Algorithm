# N진수 게임

[출처 - Programmers](https://programmers.co.kr/learn/courses/30/lessons/17687)

###### 문제 설명

튜브가 활동하는 코딩 동아리에서는 전통적으로 해오는 게임이 있다. 이 게임은 여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임인데, 규칙은 다음과 같다.

1. 숫자를 0부터 시작해서 차례대로 말한다. 첫 번째 사람은 0, 두 번째 사람은 1, … 열 번째 사람은 9를 말한다.
2. 10 이상의 숫자부터는 한 자리씩 끊어서 말한다. 즉 열한 번째 사람은 10의 첫 자리인 1, 열두 번째 사람은 둘째 자리인 0을 말한다.

이렇게 게임을 진행할 경우,
`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, …`
순으로 숫자를 말하면 된다.

한편 코딩 동아리 일원들은 컴퓨터를 다루는 사람답게 이진수로 이 게임을 진행하기도 하는데, 이 경우에는
`0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, …`
순으로 숫자를 말하면 된다.

이진수로 진행하는 게임에 익숙해져 질려가던 사람들은 좀 더 난이도를 높이기 위해 이진법에서 십육진법까지 모든 진법으로 게임을 진행해보기로 했다. 숫자 게임이 익숙하지 않은 튜브는 게임에 져서 벌칙을 받는 굴욕을 피하기 위해, 자신이 말해야 하는 숫자를 스마트폰에 미리 출력해주는 프로그램을 만들려고 한다. 튜브의 프로그램을 구현하라.

### 입력 형식

진법 `n`, 미리 구할 숫자의 갯수 `t`, 게임에 참가하는 인원 `m`, 튜브의 순서 `p` 가 주어진다.

- 2 ≦ `n` ≦ 16
- 0 ＜ `t` ≦ 1000
- 2 ≦ `m` ≦ 100
- 1 ≦ `p` ≦ `m`

### 출력 형식

튜브가 말해야 하는 숫자 `t`개를 공백 없이 차례대로 나타낸 문자열. 단, `10`~`15`는 각각 대문자 `A`~`F`로 출력한다.

### 입출력 예제

| n    | t    | m    | p    | result             |
| ---- | ---- | ---- | ---- | ------------------ |
| 2    | 4    | 2    | 1    | "0111"             |
| 16   | 16   | 2    | 1    | "02468ACE11111111" |
| 16   | 16   | 2    | 2    | "13579BDF01234567" |

[해설 보러가기](http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/)



### Code

```python
info_16 = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

def getBase_N(n,i):
    convert_n = []
    if i == 0:
        return [0]
    while i != 0:
        r = i%n
        m = i//n
        # print("r:",r,"m:",m)
        i=m
        if r > 9:
            r = info_16[r]
        convert_n.append(str(r))
    return reversed(convert_n)

def solution(n,t,m,p):
    ans = []
    i=0
    now = 0 # 사람 순서를 의미
    count = 0
    while t >= count:
        # print("count",len(count),t)
        cn = getBase_N(n,i)
        for c in cn:
            # print((now%m)+1,c)
            if (now%m)+1 == p: #튜브 차례!
                # print("Tube Turn!")
                ans.append(str(c))
                count+=1
                if count == t:
                    break
            now+=1
        i+=1
    return "".join(ans[:t])
```

### Solution

`+1`

`getBase_N` 은 우선 n진수 변환했을 때 나오는 수를 배열로 리턴 

> ex) 15 -> ["F"], 16 -> ['1','0']

0 부터 쭉 검사를 하는데 `(now%m)+1` 이 `p`와 같다면 튜브의 차례이므로 그때 해당하는 문자를 ans에 넣어준다.

시간이 오래걸린 이유는 처음에 while문의 break 조건에서 `len(count)` 를 쓰기도 했다. (하지만 고작 2ms 줄어듬)

걸리는 곳은 무수히 많을 것 이다...