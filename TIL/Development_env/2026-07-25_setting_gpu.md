# [TIL] 2026-07-25 Ubuntu 환경에서 GPU 사용을 위한 설정

## 1. 오늘 배운 것
- Ubuntu 환경에서 GPU 사용을 위한 설정 방법

## 2. 개발 환경 구성 요약
- OS : Ubuntu 24.04

## 3. 주요 설정 단계 및 명령어
### 단계 1: 기존 드라이버 정리 및 필수 패키지 설치
- 터미널에서 패키지 목록 업데이트한 뒤, 드라이버 호환성 확인 도구 설치
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential build-essential dkms ubuntu-drivers-common
```

### 단계2: NVIDIA 드라이버 설치
1. 사용 가능한 드라이버 목록과 권장 버전 확인
```bash
ubuntu-drivers devices
```
2. 권장 드라이버 설치(혹은 원하는 버전 지정 설치)
```bash
# 자동 권장 설치 - 주의 필요! 자신에게 맞는 드라이버 선택할 것
sudo ubuntu-drivers autoinstall
# 또는 특정 버전 지정 설치
sudo apt install -y nvidia-driver-535
```
**주의 사항: Secure Boot(보안 부팅) 관련**
- 메인 보드의 Secure Boot가 켜져 있으면 커널 모듈 서명 문제로 드라이버를 로드하다 부팅이 멈출 수 있다.
- 드라이버 설치 중 MOK 비밀번호 설정 화면이 나오면, 비밀번호 꼭 기억하기.
- 재부팅 시 주황/파란색 설정 화면이 나오면 `Enroll MOK` -> `Continue` -> `Yes` -> `방금 설정한 비밀번호 입력` 순으로 진행해야 드라이버 정상 로드 가능
- MOK 설정이 번거로울 경우, PC 재부팅 시 BIOS 진입, `Secure Boot` 항목을 `Disabled`로 끄기 권장.

3. 시스템 재부팅
```bash
sudo reboot
```
4. 재부팅 후 GPU 인식 확인
```bash
nvidia-smi
```

### 단계3: 가상환경(conda, .venv 등) 구축
- 시스템 레벨에서 CUDA,cuDNN 등 직접 설치 시, 버전 관리가 복잡해진다.
- os 상에는 최신 NVIDIA 그래픽 드라이버만 설치해 두고, PyTorch/TensorFlow 등을 Pip/Conda로 설치할 때 포함되는 CUDA 라이브러리를 사용하는 것이 가장 깔끔하고 오류가 적다.

### 단계4: PyTorch 및 CUDA 라이브러리 설치
```bash
# 예시 (PyTorch CUDA 12.1 버전)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 단계5: CPU 인식 확인
```bash
python3 -c "import torch; print('CUDA Available:', torch.cuda.is_available()); print('Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None')"
```
- 출력 결과: `CUDA Available: True`가 찍히면 세팅 완료

## 트러블슈팅

### 에러 발생 및 현상
- 상황: 재부팅 시 시간 지연 문제
- 에러 메시지: 재부팅(gram과 ubuntu 화면만 나오는 검은 환경)
- 해결 방법: 강제 종료 후 부팅 시도
- 결과 및 배운 점: 
    - 재부팅 시 보통 1~2분 이내로 켜져야 함.
    - 재부팅 되어 드라이버가 설치된 것을 확인 필요.
    - 재부팅 된 화면이 더 선명해보인다. 드라이버가 업데이트되며 색상/해상도 설정이 최적화되었기 때문.

- 상황: 부팅 시 ubuntu 화면에서 무한 로딩(멈춤)
- 에러 메시지: 부팅 화면 무한 대기
- 해결 방법:
    1. 강제 종료 후 Advanced options for ubuntu > Ubuntu, with Linux 6.2.0-26 generic (recovery mode) > resume > 진입
    2. 기존 설치한 nvidia driver 관련 모두 삭제
    3. reboot 해서
```bash
# 설치된 드라이버 확인
apt --installed list | grep nvidia-driver
# 설치된 드라이버 삭제
sudo apt remove nvidia-driever-595-open
sudo apt autoremove
# nvidia 관련 내용 모두 삭제
sudo apt-get remove --purge nvidia\*
sudo apt-get remove --purge nvidia*
sudo apt-get remove --purge nvidia-*
sudo apt-get remove --purge nvidia-\*
sudo apt-get remove --purge libvidia*
sudo apt-get remove --purge '^nvidia-.*'
```
- 결과 및 배운 점: 
    - 드라이버 설치 시, 본인의 GPU와 맞지 않는 버전을 설치하면 부팅 단계부터 에러가 발생한다.
    - 현재(2026-07-25 기준) ubuntu 드라이버가 안정화된 버전은 535, 550 버전이다.