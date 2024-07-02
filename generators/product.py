from faker import Faker
import json
import random
count = 0
fake = Faker()
from connections.connection import get_connection
from faker import Faker
fake = Faker()


                        
                                          


pgcursor,pgconn = get_connection()

def product_func():
    with open('product.json', 'a') as f:
        
        Faker.seed(0)
        for _ in range(50):
        
            with open('product.json', 'a') as f:
                product_id = fake.pyint(5)
                product_name = fake.first_name_male()
                product_discription = fake.lexify(text='??????????????????????????????')
                cost = fake.pyfloat(min_value=1, max_value=500,right_digits=3)
                price = cost * random.uniform(1.1,1.7)
                r = fake.profile()
                date = fake.date()
                
                
                c = {"product_id": product_id,"product_name": product_name,"product_discription":product_discription,"cost": cost,"price":price} 
                with open('product.json', 'a') as f:     
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

    


