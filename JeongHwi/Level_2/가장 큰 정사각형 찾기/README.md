# 가장 큰 정사각형 찾기

[출처 - Programmers](https://programmers.co.kr/learn/courses/30/lessons/12905)

###### 문제 설명

1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

예를 들어

|  1   |  2   |  3   |  4   |
| :--: | :--: | :--: | :--: |
|  0   |  1   |  1   |  1   |
|  1   |  1   |  1   |  1   |
|  1   |  1   |  1   |  1   |
|  0   |  0   |  1   |  0   |

가 있다면 가장 큰 정사각형은

|  1   |  2   |  3   |  4   |
| :--: | :--: | :--: | :--: |
|  0   | `1`  | `1`  | `1`  |
|  1   | `1`  | `1`  | `1`  |
|  1   | `1`  | `1`  | `1`  |
|  0   |  0   |  1   |  0   |

가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.

##### 제한사항

- 표(board)는 2차원 배열로 주어집니다.
- 표(board)의 행(row)의 크기 : 1,000 이하의 자연수
- 표(board)의 열(column)의 크기 : 1,000 이하의 자연수
- 표(board)의 값은 1또는 0으로만 이루어져 있습니다.

------

##### 입출력 예

| board                                     | answer |
| ----------------------------------------- | ------ |
| [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]] | 9      |
| [[0,0,1,1],[1,1,1,1]]                     | 4      |

##### 입출력 예 설명

입출력 예 #1
위의 예시와 같습니다.

입출력 예 #2
| 0 | 0 | `1` | `1` |
| 1 | 1 | `1` | `1` |
로 가장 큰 정사각형의 넓이는 4가 되므로 4를 return합니다.



### Code

```python
def solution(board):
    ylen = len(board)
    if ylen == 1:
        if 1 in board[0]:
            return 1
        else:
            return 0
    xlen = len(board[0])
    maxSize = -1
    for y in range(ylen):
        for x in range(xlen):
            if y == 0 or x == 0:
                continue
            if board[y][x] != 0:
                board[y][x] = min(board[y-1][x-1],board[y][x-1],board[y-1][x])+1
            maxSize = max(board[y][x],maxSize)
    return maxSize**2
```

### Solution

DP 문제이다

처음에는 Brute Force로 풀었다.

```python
def check(y,x,s,board):
    for i in range(y,y+s):
        for j in range(x,x+s):
            if board[i][j] != 1:
                return False
    return True

def solution(board):
    ylen = len(board)
    xlen = len(board[0])
    size = min(xlen,ylen)
    for s in range(size,1,-1):
        for i in range(0,ylen-(s-1)):
            for j in range(0,xlen-(s-1)):
                if board[i][j] == 0:
                    continue
                if check(i,j,s,board):
                    return s*s
                # 이 코드도 예외처리를 해주지 않아서 틀린 코드임
```

Filter Size를 기점으로 5중포문을 돌린 것, 정확성에서 성공하였다해도 효율성에서 시간초과가 난다.

질문하기에서 DP 문제라는 것을 깨닫고 DP 배열을 어떻게하면 효율적으로 구성할지를 생각해본 결과



`DP[i][j]` 는 `DP[i-1][j-1]`,`DP[i-1][j]`,`DP[i][j-1]` 중 최솟값 + 1 이라는 것을 찾아냈다.

또한 `board[i][j]`는 0이 아니어야한다. (이 조건이 중요함!), 0인 경우 `board[i][j]` 위치에서는 어떠한 정사각형도 못만들기 때문이다.

그리고 왼쪽대각선, 왼쪽, 위쪽 값을 찾았을 때 0이 있는 경우 해당 위치는 큰 정사각형이 되지 않고 그 값이 가장 큰 정사각형이므로 1이다.

점화식은 다음과 같다.
$$
DP[i][j] = min(DP[i-1][j-1],DP[i-1][j],DP[i][j-1]) +1 \ ( board[i][j] \ > \ 0)
$$

> 마크다운 $$ 로 감싸주면 수식을 작성할 수 있음



여기서 `min`인 값을 찾아내는 이유는 현재 그 자리에서 현재 만들어질 수 있는 최소 정사각형의 갯수인 것이다.

따라서 위의 예시에서 다음과 같이 표가 만들어진다.

```python
# DP
[0, 1, 1, 1]
[1, 1, 2, 2]
[1, 2, 2, 3]
[0, 0, 1, 0]
```



효율성 테스트 : `581.94ms`

`+10`