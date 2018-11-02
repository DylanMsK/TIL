# **Git**

## How to use

1. init

   1. 저장소를 만든다

2. add

   1. 임시저장 한다
   2. `git add .`을 사용해서 현재 폴더 및 하위 모든 항목을 추가
   3. `git add text.txt` 를 사용해서 원하는 파일 하나만 추가

3. commit

   1. 새로운 버전을 만든다
   2. `git commit -m '변경 내용 작성'`
   3. `git log`로 커밋 이력을 확인

4. remote

   1. 원격 저장소 설정
   2. `git remote add origin <저장소 url>` ==> origin이 아니어도 상관 없지만 통상적으로 origin 사용

5. push

   1. 내가 원하는 원격 저장소에 코드를 올리겠다
   2. `git push origin master`

6. 자주 사용하는 명령어

   1. `git status` ==> 파일/폴더의 변경 내용을 알려줌
   2. `git diff` ==> 몇번째 줄이 어떻게 바뀌었는지 알려줌
   3. `git log` ==> 커밋 이력 확인
   4. `git remote` ==> 현재 프로젝트에 등록된 원격 저장소를 확인


## Fix the error

- push가 안되는 경우([reference](http://gdtbgl93.tistory.com/63))

  `! [rejected]        master -> master (non-fast-forward)`

  1. push 하기 전에 먼저 pull을 해서 프로젝트 병합

  2. `refusing to merge unrelated histories`이 문구가 뜨고 pull이 진행되지 않으면 다음 명령으로 실행

     ```bash
     $ git pull origin <브런치명> --allow-unrelated-histories
     ```

     `--allow-unrelated-histories` 명령 옵션은 이미 존재하는 두 프로젝트의 기록(history)을 저장하는 드문 상황에 사용된다고 한다. 즉, git에서는 서로 관련 기록이 없는 이질적인 두 프로젝트를 병합할 때 기본적으로 거부하는데, 이것을 허용해 주는 것이다.

- 