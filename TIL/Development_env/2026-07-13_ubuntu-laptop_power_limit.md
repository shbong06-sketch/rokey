# [TIL] 2026-07-13 우분투 노트북 배터리 최대 충전 용량 설정

## 1. 오늘 배운 것
- 노트북 충전 용량 제한 방법(우분투, 터미널)

## 2. 개발 환경 구성 요약
- ubuntu 24.04 jazzy
- lg-gram

## 3. 주요 설정 단계 및 명령어

노트북의 배터리 설정 경로 확인 : `BAT0`
```
ls /sys/class/power_supply/
```

### 설정 단계
1. 배터리 최대 충전 용량 제한을 위한 파일 생성(혹은 수정)
```
sudo nano /etc/tmpfiles.d/batterycarelimit.conf
```

2. 해당 파일에 다음 내용 입력 : 최대 충전 용량을 80%로 설정
```
w /sys/class/power_supply/BAT0/charge_control_end_threshold - - - - 80

w /sys/class/power_supply/BAT0/charge_control_end_threshold - - - - 80

```
3. 변경 사항 적용하기(without 재부팅)
```
sudo systemd-tmpfiles --create /etc/tmpfiles.d/batterycarelimit.conf
```
4. 변경이 잘 되었나 확인 : 출력 내용이 `80`이 뜨면 성공
```
cat /sys/class/power_supply/BAT0/charge_control_end_threshold

cat /sys/devices/platform/lg-laptop/battery_care_limit
```


## 트러블슈팅

### 에러 발생 및 현상
- 상황:
- 에러 메시지:
- 해결 방법
- 결과 및 배운 점