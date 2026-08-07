# [TIL] 2026-08-07 GitHub Conflict 해결

## 1. 오늘 배운 것
- 깃허브 협업 시, 발생하는 Conflict 해결

## 2. 개발 환경 구성 요약
- Ubuntu / Git bash

## 3. 주요 설정 단계 및 명령어
### 단계 1: 원인 분석
- development 브랜치에서 분기가 된 두 브랜치(feature/so101-robot-control 와 feature/ai-model-improvement-#2) 사이에 충돌 발생
- detection_node를 초기 개발 이후, feature/ai-model-improvement-#2 브랜치에서 중간에 업데이트가 된 부분을 development 브랜치에 병합했지만, 해당 내용을 feature/so101-robot-control 브랜치에는 반영되지 않아서 동일 파일의 내용이 달라지게 되었다.

### 단계 2: 해결 단계
1. 충돌 발생 부분 확인을 위해 원격 저장소에 있는 브랜치를 내 브랜치로 가져온다.
\`\`\`bash
git switch --track origin/feature/so101-robot-control
# 브랜치 연결 상태 확인
git branch -vv
\`\`\`

2. 충돌이 난 브랜치와 비교해서 충돌 해결
```bash
# 로컬 레포지토리 업데이트
git pull origin development

# 충돌 해결을 위해 충돌이 생긴 두 브랜치를 병합시켜 충돌이 생긴 부분 해결
git checkout <충돌난 브랜치>
git merge development

# 출돌 해결이 되었다면
git push -u origin <충돌난 브랜치>
```

## 트러블슈팅

### 에러 발생 및 현상

#### 상황1
- 상황: 파일 충돌 발생
- 에러 메시지:
```
Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   ros2_ws/src/detector_node_pkg/detector_node_pkg/detector_node.py
        both added:      ros2_ws/src/robot_control_node/package.xml
        both added:      ros2_ws/src/robot_control_node/setup.py
        added by us:     ros2_ws/src/so101-ros-physical-ai~HEAD
```
파일별 충돌 내용
1. both modified : 양쪽 브랜치에서 모두 수정을 진행함.
2. both added : 양쪽 브랜치에서 모두 패키지를 새로 생성해서 동일 이름이 겹친 상황
3. Added by us : 작업 중 생긴 이름이 꼬인 파일.

- 해결 방법
1. both modified : 파일 열어 Conflict 항목 수정. 코드 누락이 되지 않도록 주의해서 수정
2. both added : 중복 내용 확인 후, 해결
3. Added by us : 해당 파일 삭제(불필요한 파일)

충돌 해결 후, `git add` 하여 Git에 충돌 해결을 알려야 한다.
상태 재확인 후, commit & push하여 해결.

#### 상황2: 
- 상황: GitHub에 올라간 브랜치 내용이 내 로컬과 달라서 안전을 위해 Git이 푸시를 막아선 상황
- 에러 메시지:
```bash
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
원격 코드를 가져오는 과정에서 로컬 브랜치와 GitHub에 올라가 있는 동일한 브랜치 간의 이력(History)이 서로 꼬였을 때 발생하는 에러.

- 해결 방법
방법1 : 강제 푸시 - 주의: 단독 작업 공간에서만 사용할 것. 다른 팀원들의 로컬 브랜치 이력과 꼬이게 된다.
```bash
git push origin [내_브랜치_이름] --force-with-lease
```
방법2: Git 정석대로 진행(`git pull`)

1. 원격 브랜치의 내용을 내 로컬 브랜치로 가져와 병합

```bash
git pull origin [내_브랜치_이름]

```
주의: git pull 이 안되는 경우 >> 로컬과 원격의 커밋 이력이 서로 꼬여서 발생. 서로 다른 갈래의 이력을 강제로 합치도록 명시해서 pull을 받아야 한다.
```bash
git pull origin feature/so101-robot-control --no-rebase

```
만약, `git pull`을 실행할 때, Git 설정에 의해 `git rebase` 방식의 풀이 실행되었다면(`git status` 입력 시, 과거 변경 내역까지 모두 나온다.), 다른 팀원의 Git 이력까지 완전히 꼬이게 만들 수 있다.
```
# 1. 진행 중인 Rebase 강제 취소
git rebase --abort

# 2단계: Merge 방식으로 안전하게 Pull 받기
git pull origin feature/so101-robot-control --no-rebase

# 3단계: Vim 또는 텍스트 차잉 뜨는 경우, 커밋 메시지 수정하지 않고 그대로 닫는다. (원격 이력과 로컬 이력을 합치는 커밋 메시지를 적으라는 창)
# Conflict 발생 시, 해당 내용 VSCode에서 확인 후, 수정하고 add & commit 하기
```

2. (만약 이 과정에서 또 충돌이 난다면 기호를 지우고 git add . -> git commit 진행) 


3. 다시 푸시 시도
```
git push origin [내_브랜치_이름]

```

- 결과 및 배운 점
충돌 해결 및 정상 병합 성공.
다양한 충돌 상황과 Rebase 설정이 꼬이게 되면 생기는 에러 메시지와 해결 방법에 대해 배울 수 있었다.