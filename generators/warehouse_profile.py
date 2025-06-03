from faker import Faker
from faker.exceptions import BaseFakerException

from connections.connection import get_conn
from connections.properties import warehouse_property_func

from faker import Faker
import pandas

pd = pandas

fake = Faker()

try:
    pgconn = get_conn()
except:
    print('connection is failing')
import json
try:
    properties1 = warehouse_property_func()
    #print(properties1)
except:
    print('no variables')


count = 0


class warehouse_profile_class():
    def warehouse_profile(self):
        try:
            Faker.seed(0)
            for _ in range(100):
                with open(properties1, 'a') as f:
                    r = fake.profile()
                    address = r['residence']
                    warehouse_id = fake.pyfloat(4)
                    c = {"warehouse_id": warehouse_id, "address": address}
                    json.dump(c, f)
                    f.write('\n')
        except BaseFakerException as err:
            print(f"Faker error generating product_id: {err}, {type(err)}")
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

    def warehouse_inserter(self, file_name, table_name):
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
