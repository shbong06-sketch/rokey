import psycopg2
import os
import time
time.sleep(5)

host = os.environ.get("DB_HOST", "db")
pw = os.environ["DB_PASSWORD"]

conn = psycopg2.connect(host=host, port=5432, dbname="robotdb",
                        user="postgres", password=pw)
cur = conn.cursor()
cur.execute("SELECT now();")

print("DB 연결 성공:", cur.fetchone()[0], flush=True)