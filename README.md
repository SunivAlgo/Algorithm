# Algorithm Study


### 목표

* Programmers 실력체크 Level3 통과

* 후에 취업 코딩테스트를 통과할 정도의 수준까지



### 방식

* 일주일에 1번 코드리뷰 및 어려운 점을 공유
  
  * 어렵다고 생각했던 문제에 대해서 질문 및 답변
* 일주일 총 10문제 (21-01-18 현재 기준)
* Git에 각자 폴더에 올리기
  * PR - Pull Request는 `이정휘` 가 맡아서 함
  * PR에 관한 내용은 "[여기](https://blog.naver.com/sowew54/222197409969)"를 참고

* 자신이 푼 방식을 마크다운이나 블로그에 정리하기

  * [예시](https://github.com/SunivAlgo/Algorithm/tree/main/JeongHwi/Level_2/%EB%8B%A4%EB%A6%AC%EB%A5%BC%20%EC%A7%80%EB%82%98%EB%8A%94%20%ED%8A%B8%EB%9F%AD)

  

#### Git Pull Request

**Init**

* `git clone https://github.com/SunivAlgo/Algorithm.git`
* Clone 시 main(master)에 있는 파일을 복사함

**Branch 추가**

* `git checkout -b [자기이름]`

**내용 추가**

1. Change Branch
   * `git checkout [Branch]`
   * 이 경우는 현재 `main` 브랜치 라면 할 것
2. 파일 추가(작업)
3. add
   * `git add .` 
     * `.` 은 버전관리할 파일 전부를 의미함
4. commit
   * `git commit -m "커밋메시지"`
   * `commit message` 예시 : `[JeongHwi] 괄호 변환 update`
5. Push
   
   * `git push origin [Branch]`
6. Merge
   * `git checkout main`
   * `git pull origin main`
   * `git merge [Branch] -m "merge Message"`
     * `merge message` 예시 : `[JeongHwi] 괄호 변환 Update`
   * `git push origin main`
   * `git checkout [branch]`
     * 다음 작업할 때 바로 add 할 수 있기 위함
   
   * `git pull origin main`
     * 이는 현재 브랜치가 내 브랜치인 경우에 해준다
     * github에 있는 저장소와 내 로컬파일을 맞춰주기 위함

>  전체 파일이 있는게 정상입니다.





