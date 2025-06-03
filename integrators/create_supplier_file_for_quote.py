import sys
from shlex import quote
from venv import create
import os
from connections.connection import get_connection
from connections.properties import create_supplier_for_quote
from connections.properties import docker_test
d = docker_test()
import pandas
import json

from multiprocessing import Pool


from integrators.create_supplier_file_for_quote2 import quote_class


sys.setrecursionlimit(1500)  # Adjust the number as needed


pd = pandas
from faker import Faker
fake = Faker()
file = create_supplier_for_quote()
try:
    pgcursor, pgconn = get_connection()
except:
    print('connection is failing')


class quote_class():
    def json_inserter(self):


        postgreSQL_select_Query = "select * from profile_"


        with pgconn.cursor() as pgcursor:
            pgcursor.execute(postgreSQL_select_Query)
            profile_records = pgcursor.fetchall()
            for row in profile_records:
                global final_file
                #print("Id = ", row[0], )
                #print("Model = ", row[1])
                #print("Price  = ", row[2])
                #print("Supplier_id  = ", row[3], "\n")
                pgcursor2 = pgconn.cursor()
                postgreSQL_select_Query1 = "SELECT * FROM vsupplier_products_questions WHERE supplier_id = " + str(row[3])
                pgcursor2.execute(postgreSQL_select_Query1)
                connect_rec = pgcursor2.fetchall()
                for row in connect_rec:
                    supplier_address  = row[0]
                    supplier_contact  = row[1]
                    supplier_company1  = row[2]
                    supplier_company = supplier_company1.translate(supplier_company1.maketrans(",- ", "___"))
                    supplier_id  = row[3]
                    supplier_email  = row[4]
                    product_id  = row[5]
                    product_name  = row[6]
                    product_discription  = row[7]
                    cost  = row[8]
                    price  = row[9]
                    question  = row[10]
                    question_id  = row[11]

                    final_file = file +'supplier_'+ supplier_company + '.json', 'a'
                    final_file_docker =  '/inv_mgmt/send_to_suppliers/'+'supplier_'+ supplier_company + '.json', 'a'


                    return final_file_docker


                    with open(final_file_docker) as f:
                        c = {"supplier_address": supplier_address,"supplier_contact": supplier_contact,"supplier_company":supplier_company,"supplier_id": supplier_id,"supplier_email":supplier_email,"product_id":product_id,"product_name":product_name,"product_discription":product_discription,"cost":cost,"price":price,"question":question,"question_id":question_id}
                        json.dump(c, f)
                        f.write('\n')
                        process_id = os.getpid()
                        print(process_id)





def run_parallel():

    with Pool(processes=50) as pool:
        pool.map(quote_class.json_inserter, range(50))  # 0 to 49

if __name__ == "__main__":
    run_parallel()

