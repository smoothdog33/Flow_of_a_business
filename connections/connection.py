import json
import os
import pandas as pd
import datetime
from datetime import datetime
import psycopg2





def get_connection():
    pgconn = psycopg2.connect(
    host = '0.0.0.0',
    user = 'postgres',
    password = 'mysecretpassword',
    database = 'inventory_managment',port = '5455')
    pgcursor = pgconn.cursor()
    return pgcursor,pgconn
def get_conn():
    return 'postgresql+psycopg2://postgres:mysecretpassword@0.0.0.0:5455/inventory_managment'