from faker import Faker 
import json

count = 0
from connections.connection import get_connection
fake = Faker()

def warehouse_profile():
    
    with open('warehouse_profile.json', 'a') as f:
        
        Faker.seed(0)
        for _ in range(50):
            
            with open('warehouse_profile.json', 'a') as f:
                r = fake.profile()
                address = r['residence']
                warehouse_id = fake.pyfloat(4)
                c = {"warehouse_id": warehouse_id,"address":address}
                with open('warehouse_profile.json', 'a') as f:     
                    json.dump(c, f)
                    f.write('\n')


import pandas
pd = pandas
def json_inserter(file_name,table_name):
        try:
            pgcursor,pgconn = get_connection()  
        except:  
            print('connection is failing')
        pgcursor = pgconn.cursor()
       
        df = pd.read_json (file_name,lines=True)
        from sqlalchemy import create_engine
        engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@0.0.0.0:5455/inventory_managment')
        print(engine)
        
        df.to_sql(table_name, engine, if_exists = 'append', index=False)



