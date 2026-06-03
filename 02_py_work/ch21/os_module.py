# os_module.py

import os

# 1. 현재 작업 디렉토리 확인 및 변경
print("------------------------")
print(f"현재 작업 디렉로리: {os.getcwd()}")
os.chdir(r".\ch21\manage_file")
# 변경된 작업 디렉토리 확인
print(f"변경 작업 디렉로리: {os.getcwd()}")

# 2. 디렉토리 및 파일 목록 조회
print("------------------------")
# 현재 디렉토리의 파일 및 폴더 목록 출력
print(f"디렉토리 목록: {os.listdir(".")}")

# 3. 디렉토리 생성 및 삭제
print("------------------------")
# os.mkdir("test_dir")
# os.rmdir("test_dir")
# print(f"디렉토리 목록: {os.listdir(".")}")

# 4. 파일 존재 여부 확인
print("------------------------")
if os.path.exists("file.txt"):
    print("파일이 존재합니다.")

# 5. 파일 및 디렉토리 경로 다루기
print("------------------------")
folder = os.getcwd()
print(folder)

cwd_file = os.path.join(folder, "file.txt")
print(cwd_file)     # 경로 합치기
# print(os.path.basename(r"C:\rokey\py_work\ch21\manage_file\file.txt"))
print(os.path.basename(cwd_file))   # 파일명만 추출
print(os.path.dirname(cwd_file))    # 디렉토리 경로 추출