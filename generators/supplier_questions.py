import json

from faker.exceptions import FakerException

from connections.connection import get_connection

from faker import Faker
fake = Faker()
import pandas
pd = pandas
from connections.connection import get_conn
from connections.properties import questions_property_func
from connections.properties import counts_of_generations



try:
    pgconn = get_conn()
except:
    print('connection is failing')

try:
    properties1 = (questions_property_func())
    #print(properties1)
except:
    print('no variables')

try:
    question_count = counts_of_generations()

except:
    print('no variables')
class supplier_questions_class():
    def supplier_questions(self):
        try:
            count = 0
            fake = Faker("en_US")
            profile = fake.profile()
            Faker.seed(5)
            for _ in range(20):
                with open(properties1, 'a') as f:
                    question_id = fake.pyint(5)
                    a = fake.lexify(text='??????????')
                    c = {"question": a, "question_id": question_id}
                    json.dump(c, f)
                    f.write('\n')

        except FakerException as err:
            print(f"Faker error generating product_id: {err}, {type(err)}")
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")




    def question_inserter(self,file_name,table_name):
        try:
            df = pd.read_json (file_name,lines=True)
            from sqlalchemy import create_engine
            engine = create_engine(pgconn)
            print(engine)

            df.to_sql(table_name, engine, if_exists = 'append', index=False)

        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except TimeoutError as e:
            print(f"Timeout error: {e}")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")



