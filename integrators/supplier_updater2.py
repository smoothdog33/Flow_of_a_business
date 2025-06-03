import threading

from connections.connection import get_connection
from connections.connection import release_connection

from multiprocessing import Pool
import os
from future.backports.datetime import datetime
from psycopg2 import OperationalError
import time
import sys
sys.setrecursionlimit(1500)  # Adjust the number as needed


from faker import Faker
fake = Faker()
class supplier_updater_class2():
    def select_func(self):

        pgcursor,pgconn = get_connection()

        pgcursor.execute('select responses_id, price from public."responses_from_supplier"')
        result = pgcursor.fetchall()
        #print("total responses from supplier" + str(result.count(0)))
        #print(datetime.now())
        with Pool(processes=100) as pool:  # Adjust the number of processes as needed
            pool.map(supplier_updater_class2.update_func, result)
        #print(datetime.now())
            #return(can_supply_test,offer_prices,response_id)
    def update_func(record):
        try:
            #print(response_id)
            response_id, price = record
            #print(response_id)
            process_id = os.getpid()
            print (process_id)
            pgcursor,pgconn = get_connection()
            offer_prices =  float(price)  * float((fake.pydecimal(max_value=1, min_value=0.5)))
            #print("something is wrong with the math, there was an arithmitic error")
            can_supply_test = fake.boolean(chance_of_getting_true=50)
            sql = "UPDATE responses_from_supplier SET can_supply=  " +  str(can_supply_test) +", offer_price = "+ str(offer_prices) +" where responses_id = '" + response_id + "'"
            #+ ", offer_price= " + str(offer_prices)+ ", responses_id =" + (responses_ids)
            print(sql)
            pgcursor.execute(sql)
            pgconn.commit()
            print(sql)
        except OperationalError as e:

            time.sleep(1)  # Wait before retrying

            raise e  # Reraise the exception if all retries failed

        finally:
            # Ensure the cursor is closed and the connection is released
            if pgcursor:
                pgcursor.close()
            if pgconn:
                release_connection(pgconn)


            #in this forloop  we are going to use the reswponse id to update the table  and set the offer price and can supply to some randomm responses


            #write another sql statement that will update the same table and set those 2 columns with random values
            # go make another create script for update sql
            # after i have the update sql reday in python execte the sql in that forloop
        #max_m_time= result [0][2]
        ##max_c_time= result [0][3]
        #run_id= result [0][4]

        # from this data set we will find the bset suplier for each product.
        #take all python files and put it into git in a proper way

        #do the git connection to vs code thing
if __name__ == "__main__":

    supplier_updater_class2.select_func(None)





