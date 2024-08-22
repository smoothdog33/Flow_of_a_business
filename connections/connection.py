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
    password = 'postgres',
    database = 'inventory_managment',port = '5432')
    pgcursor = pgconn.cursor()
    return pgcursor,pgconn
def get_conn():
    return 'postgresql+psycopg2://postgres:postgres@0.0.0.0:5432/inventory_managment'


