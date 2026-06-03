# mex4.py
# 메인 모듈
import mex2
# 같은 경로의 파일 불러오기
# 별도의 경로 적을 필요 X
print(mex2.mul(2, 3))


# import 패키지명.모듈명
import ch10_1.mex2

print(ch10_1.mex2.minus(4, 2))

# import 사용 시
# 현재 작업 폴더에서 사용 가능
# 현재 위치가 어디에 있는지 알아야 한다.
# 현재 파일 기준으로 하위폴더로 접근 가능.


# import ch09.Bag   # error: 상위 경로 파악 X

# cross = ch09.Bag("크로스백", "갈색")
# print(cross.color)


# 디렉터리 : 폴더(파일과 다른 폴더를 구분/저장하는 단위)
# 패키지 : 파이썬이 '모듈 집합'으로 인식하는 폴더

# 상위 경로의 모듈 활용
# 1. import는 같은 패키지 내에서 활용
# 2. 하위 경로에서 활용 => import 패키지명.모듈명
# 3. 상위 경로에서 활용 => 제한적 활용이 가능(라이브러리 활용)
#    : sys.path 라이브러리 활용
# 4. 실무에서 활용 방법 : 상위 경로 접근을 원천적으로 차단

# 예시) 실무에서 파일 경로 구성
# project
#  - src(소스 경로)
#    - myapp
#       - __init__.py ; 내부 경로 파악하다가 각 모듈의 위치를 하위모듈에서 인식해서 사용할 수 있게 알려주는 역할(내용 필요X)
#       - main.py
#       - core
#           - logic.py
#       - utility
#            - help.py
#       - db
#            -model.py
#  - test
#  - 라이브러리
#  - READ_ME