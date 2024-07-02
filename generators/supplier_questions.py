import json
from connections.connection import get_connection
from faker import Faker
fake = Faker()
import pandas
pd = pandas
from connections.connection import get_conn

try:
    pgconn = get_conn()
except:
    print('connection is failing')


class supplier_questions_class():
    def supplier_questions(self):
        count = 0
        fake = Faker("en_US")
        profile = fake.profile()
        Faker.seed(5)
        for _ in range(20):
            with open('/Users/ayan/IdeaProjects/target/data/questions.json', 'a') as f:
                question_id = fake.pyint(5)
                a = fake.lexify(text='??????????')
                c = {"question": a, "question_id": question_id}
                json.dump(c, f)
                f.write('\n')



    def question_inserter(self,file_name,table_name):

            df = pd.read_json (file_name,lines=True)
            from sqlalchemy import create_engine
            engine = create_engine(pgconn)
            print(engine)

            df.to_sql(table_name, engine, if_exists = 'append', index=False)


