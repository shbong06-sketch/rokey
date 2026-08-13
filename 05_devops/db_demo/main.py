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
cur.execute("select * from cafe_customers;")
# fetch results
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()