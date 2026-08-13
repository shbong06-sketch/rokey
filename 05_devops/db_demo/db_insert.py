import psycopg2
from dotenv import load_dotenv
import os

# Connect to the PostgreSQL database
load_dotenv()
conn = psycopg2.connect(
    # host, port, id, pw, dbname
    host = os.getenv('HOST'),
    port = os.getenv('PORT'),
    database = os.getenv('DB_NAME'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD')
)
# Cursor를 통해 연결된 DB와 상호작용
cur = conn.cursor()

# Execute SQL queries
# cur.execute("insert into cafe_customers (name, phone) values ('John Doe', '010-2222-2222');") # 하드 코딩
customer_name = input("Enter customer name: ")
customer_phone = input("Enter customer phone: ")
cur.execute("insert into cafe_customers (name, phone) values (%s, %s);", (customer_name, customer_phone))


# CRUD -> CUD / R 구분 필요
# CUD(데이터 변경이 있는 작업) -> commit 필요
conn.commit()

cur.close()
conn.close()