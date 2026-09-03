# DB 연결 객체 생성 및 컬렉션 선택
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# .env 파일에서 환경 변수 가져오기
mongo_uri = os.environ["MONGO_URI"]
database_name = os.getenv(
    "MONGO_DATABASE",
    "kit_tracking",
)

# MongoDB 연결 객체 생성 - DB client 생성
client = MongoClient(
    mongo_uri,
    # 연결 실패 시 최대 5초 대기
    serverSelectionTimeoutMS=5000,
    # 조회한 시간을 시간대 정보가 있는 값으로 처리
    tz_aware=True,
)

db = client[database_name]

# commands 컬랙션 선택
commands = db["commands"]
component_executions = db["component_executions"]
kit_executions = db["kit_executions"]


def check_connection():
    """MongoDB 서버 연결 상태를 확인한다."""
    # 실제 서버 응답 확인
    return client.admin.command("ping")


def close_connection():
    """MongoDB 클라이언트 연결을 종료한다."""
    client.close()