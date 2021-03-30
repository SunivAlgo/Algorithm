# 자물쇠와 열쇠

###### 문제 설명

고고학자인 **"튜브"**는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 그런데 문을 열려고 살펴보니 특이한 형태의 **자물쇠**로 잠겨 있었고 문 앞에는 특이한 형태의 **열쇠**와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

잠겨있는 자물쇠는 격자 한 칸의 크기가 **`1 x 1`**인 **`N x N`** 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 **`M x M`** 크기인 정사각 격자 형태로 되어 있습니다.

자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
- lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
- M은 항상 N 이하입니다.
- key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
  - 0은 홈 부분, 1은 돌기 부분을 나타냅니다.

------

### 입출력 예

| key                               | lock                              | result |
| --------------------------------- | --------------------------------- | ------ |
| [[0, 0, 0], [1, 0, 0], [0, 1, 1]] | [[1, 1, 1], [1, 1, 0], [1, 0, 1]] | true   |

### 입출력 예에 대한 설명

![자물쇠.jpg](figure/README/79f2f473-5d13-47b9-96e0-a10e17b7d49a.jpg)

key를 시계 방향으로 90도 회전하고, 오른쪽으로 한 칸, 아래로 한 칸 이동하면 lock의 홈 부분을 정확히 모두 채울 수 있습니다.

------

혼자 풀기가 막막하다면, 풀이 강의를 들어보세요 [(클릭)](https://programmers.co.kr/learn/courses/10336?utm_source=programmers&utm_medium=test_course10336&utm_campaign=course_10336)

### Code

[답 참고 하였음](https://medium.com/@dltkddud4403/2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%B8%94%EB%9D%BC%EC%9D%B8%EB%93%9C-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-47c2846da576)

```Python
import copy
def getRotate(keys,m): # Rotate 90 Degree.
    result = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m-i-1] = keys[i][j]
    return result

def check(n,m,pad,key,i,j,lockS):
    temp = copy.deepcopy(pad)
    for y in range(m):
        for x in range(m):
            temp[y+i][x+j] = temp[y+i][x+j]^key[y][x]
    
    
    for y in range(m-1,m-1+n):
        for x in range(m-1,m-1+n):
            if temp[y][x] == 0:
                return False
    return True

def adj_Padding(lock,n,keys,m):
    # m+n-2, Padding
    pad = [[0 for _ in range(n+m*2-2)] for _ in range(n+m*2-2)]
    for i in range(m-1,n+m-1):
        for j in range(m-1,n+m-1):
            pad[i][j] = lock[i-m+1][j-m+1]
    
    lockS = m-1
    for k in keys:
        for i in range(n+m-1):
            for j in range(n+m-1):
                if check(n,m,pad,k,i,j,lockS):
                    return True
    return False
                    


def solution(key,lock):
    m = len(key)
    n = len(lock)
    
    ro_90_key = getRotate(key,m)
    ro_180_key = getRotate(ro_90_key,m)
    ro_270_key = getRotate(ro_180_key,m)

    keys = [key,ro_90_key,ro_180_key,ro_270_key]
    return adj_Padding(lock,n,keys,m)
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
```

### Solution

답을 참고하였다.

이 문제는 완전 탐색 구현 문제이다. 하지만 어려운 구현문제였다..

간단하게 생각하면 4방향으로 돌린 키를 padding을 씌운 lock에다 하나씩 체크를 하는 것이다 (1개 겹칠때부터)

하지만 Padding을 씌우는 과정이 어렵다.. key의 크기와 lock의 크기를 잘 조합해서 해야한다..

따라서 `n+m*2-2` 라는 식이 나왔다. 이식은.. 외우자!

그래서 padding을 씌운 lock에 Key를 하나씩 XOR 연산 (`^`) 으로 계산하여 `temp`라는 Padding Lock의 복사본에 저장한다.

Key 를 씌운 연산이 끝나면 lock을 검사한다. (lock의 위치를 기억한다! `m-1 ~ m+n-1`)

그래서 lock이 모두 1이면 Return True

좀 어려운 문제였다. (90도 돌리는 코드도 기억해두면 좋을듯)

`+2`