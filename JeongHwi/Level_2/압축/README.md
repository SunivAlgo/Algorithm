# 압축

[출처 - Programmers](https://programmers.co.kr/learn/courses/30/lessons/17684)

###### 문제 설명

신입사원 어피치는 카카오톡으로 전송되는 메시지를 압축하여 전송 효율을 높이는 업무를 맡게 되었다. 메시지를 압축하더라도 전달되는 정보가 바뀌어서는 안 되므로, 압축 전의 정보를 완벽하게 복원 가능한 무손실 압축 알고리즘을 구현하기로 했다.

어피치는 여러 압축 알고리즘 중에서 성능이 좋고 구현이 간단한 **LZW**(Lempel–Ziv–Welch) 압축을 구현하기로 했다. LZW 압축은 1983년 발표된 알고리즘으로, 이미지 파일 포맷인 GIF 등 다양한 응용에서 사용되었다.

LZW 압축은 다음 과정을 거친다.

1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 `w`를 찾는다.
3. `w`에 해당하는 사전의 색인 번호를 출력하고, 입력에서 `w`를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(`c`), `w+c`에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다.

압축 알고리즘이 영문 대문자만 처리한다고 할 때, 사전은 다음과 같이 초기화된다. 사전의 색인 번호는 정수값으로 주어지며, 1부터 시작한다고 하자.

| 색인 번호 | 1    | 2    | 3    | ...  | 24   | 25   | 26   |
| --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 단어      | A    | B    | C    | ...  | X    | Y    | Z    |

예를 들어 입력으로 `KAKAO`가 들어온다고 하자.

1. 현재 사전에는 `KAKAO`의 첫 글자 `K`는 등록되어 있으나, 두 번째 글자까지인 `KA`는 없으므로, 첫 글자 `K`에 해당하는 색인 번호 11을 출력하고, 다음 글자인 `A`를 포함한 `KA`를 사전에 27 번째로 등록한다.
2. 두 번째 글자 `A`는 사전에 있으나, 세 번째 글자까지인 `AK`는 사전에 없으므로, `A`의 색인 번호 1을 출력하고, `AK`를 사전에 28 번째로 등록한다.
3. 세 번째 글자에서 시작하는 `KA`가 사전에 있으므로, `KA`에 해당하는 색인 번호 27을 출력하고, 다음 글자 `O`를 포함한 `KAO`를 29 번째로 등록한다.
4. 마지막으로 처리되지 않은 글자 `O`에 해당하는 색인 번호 15를 출력한다.

| 현재 입력(w) | 다음 글자(c) | 출력 | 사전 추가(w+c) |
| ------------ | ------------ | ---- | -------------- |
| K            | A            | 11   | 27: KA         |
| A            | K            | 1    | 28: AK         |
| KA           | O            | 27   | 29: KAO        |
| O            |              | 15   |                |

이 과정을 거쳐 다섯 글자의 문장 `KAKAO`가 4개의 색인 번호 [11, 1, 27, 15]로 압축된다.

입력으로 `TOBEORNOTTOBEORTOBEORNOT`가 들어오면 다음과 같이 압축이 진행된다.

| 현재 입력(w) | 다음 글자(c) | 출력 | 사전 추가(w+c) |
| ------------ | ------------ | ---- | -------------- |
| T            | O            | 20   | 27: TO         |
| O            | B            | 15   | 28: OB         |
| B            | E            | 2    | 29: BE         |
| E            | O            | 5    | 30: EO         |
| O            | R            | 15   | 31: OR         |
| R            | N            | 18   | 32: RN         |
| N            | O            | 14   | 33: NO         |
| O            | T            | 15   | 34: OT         |
| T            | T            | 20   | 35: TT         |
| TO           | B            | 27   | 36: TOB        |
| BE           | O            | 29   | 37: BEO        |
| OR           | T            | 31   | 38: ORT        |
| TOB          | E            | 36   | 39: TOBE       |
| EO           | R            | 30   | 40: EOR        |
| RN           | O            | 32   | 41: RNO        |
| OT           |              | 34   |                |

### 입력 형식

입력으로 영문 대문자로만 이뤄진 문자열 `msg`가 주어진다. `msg`의 길이는 1 글자 이상, 1000 글자 이하이다.

### 출력 형식

주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력하라.

### 입출력 예제

| msg                        | answer                                                       |
| -------------------------- | ------------------------------------------------------------ |
| `KAKAO`                    | [11, 1, 27, 15]                                              |
| `TOBEORNOTTOBEORTOBEORNOT` | [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34] |
| `ABABABABABABABAB`         | [1, 2, 27, 29, 28, 31, 30]                                   |

[해설 보러가기](http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/)



### Code

```python
import string
def solution(msg):
    # Uppercase Dictionary
    dics = dict([(x,i+1) for i,x in enumerate(string.ascii_uppercase)])
    dics_num = 26
    ans = []

    msglen = len(msg)
    target = ""
    for i in range(0,msglen):
        if i == msglen-1: # Last alphabet check
            ans.append(dics[target+msg[i]])
            break

        target+=msg[i]
        if target+msg[i+1] in dics: # word in Dictionary
            # print("in Dict",target)
            continue
        else: # not in Dictionary
            dics_num+=1
            dics[target+msg[i+1]] = dics_num
            ans.append(dics[target])
            target = ""

    
    return ans
```

### Solution

의외로 3차 문제 치고는 간단했던 문제

우선 `Key : Value` 쌍을 `"A": 1` 이런식으로 맞춰주었다.

그리고 `target`을 설정하였는데, `target`은 해당 문자열이 `dics`안에 존재하는지 확인하는 용도다.

`KAKAO`를 예시로 들어보자.

| Alphabet          | K       | A       | K    | A        | O    |
| ----------------- | ------- | ------- | ---- | -------- | ---- |
| target            | K       | A       | K    | KA       | O    |
| target+msg[i+1]   | KA      | AK      | KA   | KAO      | -    |
| Insert Dictionary | KA : 27 | AK : 28 | -    | KAO : 29 | -    |
| output            | 11      | 1       | -    | 27       | 15   |

* 우선 `target+msg[i+1]` 이 dictionary 안에 존재하면 `continue`를 시킨다, 따라서 2번째 `K`에서 `KA` 가 이미 Dictionary 안에 존재하기 때문에 `continue` 되었고 그 다음 `target+msg[i+1]`인 `KAO`를 다시 체크한다.

* `target+msg[i+1]` 이 없는 단어라면 해당 단어를 dictionary에 순서대로 넣어준다. 

  > `dics_num` 은 dictionray Len를 추적하는 변수

* output은 이어지는 단어가 없을 경우에 `dics[target]`이 된다.



`+1`

> 어려웠던 부분은 ... ABCDEFGHI....를 어떻게 dict화 시키느냐가 가장 난감했다.