import json
import os

from connections.connection import get_connection
from faker import Faker

fake = Faker()
try:
    pgcursor, pgconn = get_connection()
except:
    print('connection is failing')


def responses_inserter(sql):
    pgconn.autocommit = True
    with pgconn.cursor() as pgcursor:

        pgcursor.execute(sql)



class responses_class():


    #pgconn = get_conn()

    def load_responses(self,input_directory):
        responses_id = 0
        print("hiii")
        print(input_directory)
        for root, dirs, files in os.walk(input_directory):
            for file in files:
                path_creator = os.path.join(root,file)
                file_abs_path = os.path.abspath(path_creator)

                with open(file_abs_path, 'r', encoding='windows-1252') as f:
                    print(file_abs_path)
                    print(" i am reading this")

                    for jsonObj in f:
                        product_dictionary = json.loads(jsonObj)
                        supplier_address = str((product_dictionary.get('supplier_adress')))
                        supplier_contact = str((product_dictionary.get('supplier_contact')))
                        supplier_company = str((product_dictionary.get('supplier_company')))
                        supplier_id = (product_dictionary.get('supplier_id'))
                        product_id = (product_dictionary.get('product_id'))
                        product_name = str((product_dictionary.get('product_name')))
                        product_discription = (str(product_dictionary.get('product_discription')))
                        cost = (product_dictionary.get('cost'))
                        price = (product_dictionary.get('price'))
                        question = str((product_dictionary.get('question')))
                        question_id = (product_dictionary.get('question_id'))
                        responses_id = (responses_id + 1)
                        sql = ("INSERT INTO public.responses_from_supplier"
                               "(supplier_address, supplier_contact, supplier_company, product_name, product_discription, question, supplier_id, product_id, cost, price, question_id,responses_id) VALUES ('") + supplier_address + "','" + supplier_contact + "','" + supplier_company + "','" + product_name +"','"+ product_discription +"','" + question +"','"+ str(supplier_id) +"','" + str(product_id)+"','"+ str(cost) + "','" + str(price) + "','"+ str(question_id) +"','" + str(responses_id) +"');"
                        responses_inserter(sql)