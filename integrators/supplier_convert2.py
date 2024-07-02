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

product_list = []
supplier_list = []

class supplier_conv_class():

    def supplier_conv(self):

        with open("/Users/ayan/IdeaProjects/target/data/supplier_profile1.json","r") as file:
            for jsonObj in file:
                supplier_dictionary = json.loads(jsonObj)
                supplier_list.append(supplier_dictionary)
                a = (supplier_dictionary.get('supplier_id'))

                with open("/Users/ayan/IdeaProjects/target/data/product.json","r") as file:
                    for jsonObj in file:
                        try:
                            product_dictionary = json.loads(jsonObj)
                            product_list.append(product_dictionary)
                            p = (product_dictionary.get('product_id'))
                            print(p)
                        except Exception as err:
                            print(f"Open Product Unexpected {err=}, {type(err)=}")

                        with open("/Users/ayan/IdeaProjects/target/data/questions.json","r") as file:
                                for jsonObj in file:
                                    try:
                                        question_dictionary = json.loads(jsonObj)
                                        d = (question_dictionary.get('question_id'))
                                        new_dict = {"supplier_1":a,"product_id":p,"question_id":d}
                                        with open('/Users/ayan/IdeaProjects/target/data/supplier_conv.json', 'a') as f:
                                                    json.dump(new_dict, f)
                                                    f.write('\n')
                                    except Exception as err:
                                         print(f"Open Questions Unexpected {err=}, {type(err)=}")

    def convert_inserter(self,file_name,table_name):
            df = pd.read_json (file_name,lines=True)
            from sqlalchemy import create_engine
            engine = create_engine(pgconn)
            print(engine)
            df.to_sql(table_name, engine, if_exists = 'append', index=False)


