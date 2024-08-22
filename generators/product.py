from faker import Faker
import json
import random
count = 0
fake = Faker()
from connections.connection import get_conn
from connections.properties import product_property_func
from connections.properties import counts_of_generations

from faker import Faker
from faker.exceptions import FakerException

import pandas
import errno
import os

pd = pandas

fake = Faker()

try:
    pgconn = get_conn()
except:
    print('connection is failing')
try:
    properties1 = product_property_func()
    #print(properties1)
except:
    print('no variables')
try:
    product_count = counts_of_generations()
    #print(properties1)
except:
    print('no variables')

class product_class():

        def product_func(self):
            try:
                with open(properties1, 'a') as f:
                    Faker.seed(0)
                    for _ in range(50):
                        product_id = fake.pyint(5)
                        product_name = fake.first_name_male()
                        product_discription = fake.lexify(text='??????????????????????????????')
                        cost = fake.pyfloat(min_value=1, max_value=500, right_digits=3)
                        price = cost * random.uniform(1.1, 1.7)
                        r = fake.profile()
                        date = fake.date()
                        c = {"product_id": product_id, "product_name": product_name, "product_discription": product_discription,
                             "cost": cost, "price": price}
                        json.dump(c, f)
                        f.write('\n')

            except FakerException as err:
                print(f"Faker error generating product_id: {err}, {type(err)}")
            except FileNotFoundError as e:
                print(f"File not found: {e}")
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")


        def product_inserter(self,file_name, table_name):
            try:
                df = pd.read_json(file_name, lines=True)
                from sqlalchemy import create_engine
                engine = create_engine(pgconn)
                print(engine)
                df.to_sql(table_name, engine, if_exists='append', index=False)
            except FileNotFoundError as e:
                print(f"File not found: {e}")
            except TimeoutError as e:
                print(f"Timeout error: {e}")
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")

