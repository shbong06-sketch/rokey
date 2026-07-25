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
# 자동 권장 설치
sudo ubuntu-drivers autoinstall
# 또는 특정 버전 지정 설치
sudo apt install -y <원하는 버전 지정>
```
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