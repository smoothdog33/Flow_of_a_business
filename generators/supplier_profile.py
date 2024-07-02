import json
from connections.connection import get_connection
from faker import Faker
fake = Faker()
try:
    pgcursor,pgconn = get_connection()  
except:  
    print('connection is failing')
def supplier_profile():
        count = 0
        fake = Faker("en_US")
        profile = fake.profile()
        Faker.seed(0)
        for _ in range(50):
            with open('supplier_profile.json', 'a') as f:
                
                supplier_contact = fake.phone_number()
                r = fake.profile()
                company_id = fake.pyint(4)
                supplier_address = r['residence']
                supplier_company = r['company']
                supplier_email = r['mail']
                c = {"supplier_address": supplier_address ,"supplier_contact": supplier_contact,"supplier_company":supplier_company,"supplier_id":company_id,"supplier_email":supplier_email}
                json.dump(c, f)
                f.write('\n')


import pandas
pd = pandas
def json_inserter(file_name,table_name):
        
       
        df = pd.read_json (file_name,lines=True)
        from sqlalchemy import create_engine
        engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@0.0.0.0:5455/inventory_managment')
        print(engine)
        
        df.to_sql(table_name, engine, if_exists = 'append', index=False)