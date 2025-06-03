import json
import os
import pandas as pd
import datetime
from datetime import datetime
import psycopg2
from psycopg2 import pool


pgconn1 = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=150,
    host = 'postgres-container',
    user = 'postgres',
    password = 'secret123',
    database = 'postgres',port = '5432')


def get_connection():
    pgconn = pgconn1.getconn()
    pgcursor = pgconn.cursor()
    return pgcursor,pgconn
def get_conn():
    return 'postgresql+psycopg2://postgres:secret123@postgres-container:5432/postgres'

def release_connection(conn):
    pgconn1.putconn(conn)
