from faker import Faker
from connections.connection import get_conn
from faker import Faker
import pandas

pd = pandas

fake = Faker()

try:
    pgconn = get_conn()
except:
    print('connection is failing')
import json

count = 0


class warehouse_profile_class():
    def warehouse_profile(self):
            Faker.seed(0)
            for _ in range(50):
                with open('/Users/ayan/IdeaProjects/target/data/warehouse_profile.json', 'a') as f:
                    r = fake.profile()
                    address = r['residence']
                    warehouse_id = fake.pyfloat(4)
                    c = {"warehouse_id": warehouse_id, "address": address}
                    json.dump(c, f)
                    f.write('\n')

    def warehouse_inserter(self, file_name, table_name):
        df = pd.read_json(file_name, lines=True)
        from sqlalchemy import create_engine
        engine = create_engine(pgconn)
        print(engine)

        df.to_sql(table_name, engine, if_exists='append', index=False)
