# [TIL] 2026-05-30 윈도우-우분투 연동 개발 환경 구축

## 1. 오늘 배운 것
- ssh: 보안 셀. 네트워크를 통해 원격으로 접속할 때 사용하는 방식
- 기기 간 연동 및 네트워크 세팅 방법(윈도우-우분투 연동 with VS Code)

## 2. 개발 환경 구성 요약
- OS : Windows / Ubuntu 22.04
- 프로그램 : VS Code(Remote-SSH)

## 3. 주요 설정 단계 명령어
### 단계1: 우분투 노트북 세팅
- 우분투 터미널을 열고, SSH 서버 설치 및 IP 주소 확인
```bash
sudo apt update && sudo apt install openssh-server
hostname -I
```

### 단계2: 윈도우 노트북 세팅
- VS Code에서 Remote -SSH 설치(확장팩)
- VS Code 좌하단의 ><(원격 창 열기) 클릭
- Connect to Host... -> Add New SSH... 선택
- ssh 우분투계정명@우분투IP주소 -> 첫 번째 경로 선택(나중에 클릭 한번으로 접속 가능)
- 비밀번호 입력하면 연결 완료


## 트러블슈팅

### 에러 발생 및 현상
- 상황: 우분투 노트북에 SSH 서버 설치 과정에 오류 발생
- 에러 메시지:
```
shbong@SHBong-Creator-15M-A9SD:~$ sudo systemctl enable --now sshd
Failed to enable unit: Unit file sshd.service does not exist
```
- 해결 방법: 
    - 다운로드 서버 변경(Kakao 주소로 변경)
    - 업데이트 다시 시도 및 SSH 서버 재설치
    - SSH 서비스 시작하기
    - 정상 작동 확인
```bash
sudo sed -i 's/kr.archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
sudo apt update && sudo apt install --reinstall openssh-server
sudo systemctl enable --now ssh
sudo systemctl status ssh
```
- 결과 및 배운 점
    - 기본 서버: kr.archive.ubuntu.com -> 일시적 오류 발생
    - 변경한 서버: mirror.kakao.com -> 국내에서 가장 관리가 잘 되고 속도가 빠른 우분투 미러 서버