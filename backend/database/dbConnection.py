import psycopg2 as postgres
import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DATABASE")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
db_port = os.getenv("PORT")
db_host = os.getenv("HOST")

conn = postgres.connect(host=db_host, port=db_port, database=db_name, user=db_user, password=db_password)
