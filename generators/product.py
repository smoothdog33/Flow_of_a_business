from faker import Faker
import json
import random
count = 0
fake = Faker()
from connections.connection import get_conn
from faker import Faker
import pandas

pd = pandas

fake = Faker()

try:
    pgconn = get_conn()
except:
    print('connection is failing')

class product_class():

        def product_func(self):
            with open('/Users/ayan/IdeaProjects/target/data/product.json', 'a') as f:

                Faker.seed(0)
                for _ in range(50):
                    product_id = fake.pyint(5)
                    product_name = fake.first_name_male()
                    product_discription = fake.lexify(text='??????????????????????????????')
                    cost = fake.pyfloat(min_value=1, max_value=500, right_digits=3)
                    price = cost * random.uniform(1.1, 1.7)
                    r = fake.profile()
                    date = fake.date()
                    print(r)

                    c = {"product_id": product_id, "product_name": product_name, "product_discription": product_discription,
                         "cost": cost, "price": price}
                    json.dump(c, f)
                    f.write('\n')





        def product_inserter(self,file_name, table_name):
            df = pd.read_json(file_name, lines=True)
            from sqlalchemy import create_engine
            engine = create_engine(pgconn)

            print(engine)

            df.to_sql(table_name, engine, if_exists='append', index=False)

