# mex3.py

from mex1 import plus
from mex1 import Cvalue
# from mex1 import p1
# 장점
# 내가 어떤 클래스나 함수를 가져다 쓰는지 명확해져
# => 코드의 가독성이 좋아져

# from 모듈명 import *
from mex1 import *
# 장점
# 많은 내용을 가져와 쓰는 경우, 간편/길이를 짧게 할 수 있다.
# 단점
# 가독성 떨어진다.
# 객체 이름이 충돌할 수 있다.

# 객체 생성
p3 = Cvalue()
p3.add(100)
p3.add(200)
p3.fprint()
print(plus(100, 200))

# 모듈명 명시 없이도 사용 가능

# print(__name__)