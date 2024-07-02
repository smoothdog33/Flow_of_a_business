import json
from connections.connection import get_connection
from faker import Faker
fake = Faker()
pgcursor,pgconn = get_connection()

def supplier_questions():
    count = 0
    fake = Faker("en_US")
    profile = fake.profile()
    Faker.seed(5)
    for _ in range(20):
        with open('questions.json', 'a') as f:
            question_id = fake.pyint(5)
            a = fake.lexify(text='??????????')
            c = {"question": a,"question_id":question_id}     
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


