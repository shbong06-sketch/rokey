# default3.py

def connect_db(host = "localhost", port = 3306, timeout = 3):
    print(host, port, timeout)

connect_db()    # 기본 연결 수행
connect_db(timeout = 10)

# 실제 기업 현장
# 아이디어 구상
# 문서화
# >> 코드화 한다.

# 아이디어와 문서화 예시
# 데이터베이스(DB) : 데이터 집합

# db에 접근하고 싶다.
# db는 같은 네트워크에 내 컴퓨터로 제어되고 있다. => 접근방법
# db에 데이터를 꺼내오려면 port를 통해서 가져와야 한다.
# 시스템에 접속해서 3초 기다렸다가 안되면 재접속 해야지.

