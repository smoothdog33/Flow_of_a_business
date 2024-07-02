import json
from connections.connection import get_conn
from faker import Faker
fake = Faker()
import pandas
pd = pandas
try:
    pgconn = get_conn()
except:  
    print('connection is failing')


class supplier_profile_class():
    def supplier_profile(self):
            count = 0
            fake = Faker("en_US")
            profile = fake.profile()
            Faker.seed(0)
            for _ in range(50):
                with open('/Users/ayan/IdeaProjects/target/data/supplier_profile1.json', 'a') as f:

                    supplier_contact = fake.phone_number()
                    r = fake.profile()
                    company_id = fake.pyint(4)
                    supplier_address = r['residence']
                    supplier_company = r['company']
                    supplier_email = r['mail']
                    c = {"supplier_address": supplier_address ,"supplier_contact": supplier_contact,"supplier_company":supplier_company,"supplier_id":company_id,"supplier_email":supplier_email}
                    json.dump(c, f)
                    f.write('\n')

    def supplier_profile_inserter(self,file_name,table_name):

            df = pd.read_json (file_name,lines=True)
            from sqlalchemy import create_engine
           # engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@0.0.0.0:5455/inventory_managment')
            engine = create_engine(pgconn)

            print(engine)

            df.to_sql(table_name, engine, if_exists = 'append', index=False)