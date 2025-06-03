from connections.connection import get_connection
from connections.properties import create_supplier_for_quote,docker_test
import pandas
import json
from multiprocessing import Pool
import os
import sys
sys.setrecursionlimit(1500)

pd = pandas

file = create_supplier_for_quote()

def quote_dumper(profile_record):
    supplier_address, supplier_id = profile_record
    try:
        pgcursor, pgconn = get_connection()
        pgcursor2 = pgconn.cursor()

        query = "SELECT * FROM vsupplier_products_questions WHERE supplier_id = %s"
        pgcursor2.execute(query, (supplier_id,))
        connect_rec = pgcursor2.fetchall()

        for row in connect_rec:
            supplier_address = row[0]
            supplier_contact = row[1]
            supplier_company1 = row[2]
            supplier_company = supplier_company1.translate(supplier_company1.maketrans(",- ", "___"))
            supplier_id = row[3]
            supplier_email = row[4]
            product_id = row[5]
            product_name = row[6]
            product_discription = row[7]
            cost = row[8]
            price = row[9]
            question = row[10]
            question_id = row[11]

            process_id = os.getpid()



        if docker_test() == 1:
            with open('/inv_mgmt/send_to_suppliers/'+'supplier_'+ supplier_company + '.json', 'a') as f:
                c = {
                    "supplier_address": supplier_address,
                    "supplier_contact": supplier_contact,
                    "supplier_company": supplier_company,
                    "supplier_id": supplier_id,
                    "supplier_email": supplier_email,
                    "product_id": product_id,
                    "product_name": product_name,
                    "product_discription": product_discription,
                    "cost": cost,
                    "price": price,
                    "question": question,
                    "question_id": question_id
                }
                json.dump(c, f)
                f.write('\n')
        else:
            with open(file +'supplier_'+ supplier_company + '.json', 'a') as f:
                c = {
                    "supplier_address": supplier_address,
                    "supplier_contact": supplier_contact,
                    "supplier_company": supplier_company,
                    "supplier_id": supplier_id,
                    "supplier_email": supplier_email,
                    "product_id": product_id,
                    "product_name": product_name,
                    "product_discription": product_discription,
                    "cost": cost,
                    "price": price,
                    "question": question,
                    "question_id": question_id
                }
                json.dump(c, f)
                f.write('\n')

        pgcursor2.close()
        pgconn.close()

    except Exception as e:
        print(f"Error in process {os.getpid()}: {e}")

class quote_class:
    def quote_select(self):
        try:
            pgcursor, pgconn = get_connection()
            postgreSQL_select_Query = "SELECT supplier_address, supplier_id FROM profile_"
            pgcursor.execute(postgreSQL_select_Query)
            profile_records = pgcursor.fetchall()
            pgcursor.close()
            pgconn.close()
        except Exception as e:
            print(f"Error fetching profile records: {e}")
            return

        with Pool(processes=5) as pool:
            pool.map(quote_dumper, profile_records)

# Usage:
if __name__ == '__main__':
    qc = quote_class()
    qc.quote_select()

