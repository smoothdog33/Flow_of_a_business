import sys
from psycopg2 import OperationalError
from connections.connection import get_connection
from faker import Faker
fake = Faker()
def print_psycopg2_exception(err):
    err_type,err_obj,traceback = sys.exc_info()
    line_num = traceback.tb_lineno

    print("\n psycopg2 ERROR:ss" , err ,"on line number:", line_num)
    print("psycopg2 tracebackss:", traceback,"-- type:",err_type)
    exit()


                        
                                          


try:
    pgcursor,pgconn = get_connection()  
except OperationalError as err:  
    print_psycopg2_exception(err)

pgcursor.execute('select product_id,price, cost  from public."products"')
result = pgcursor.fetchall()     
#supplier_address= result [0][1]


i=1
Faker.seed(0)
for r in result:
    print(r)
    product_id = r[0]
    price =  r[1]
    cost = r[2]
   #cost = round(cost,2)
    pgcursor1 = pgconn.cursor()
    
    competitive_price =  round(price  * float((fake.pydecimal(max_value=1.15, min_value=.85))),2)
    if competitive_price < cost:
        competitive_price = cost * 1.1
        print("competitive pricez" , competitive_price)
        
        sql = "UPDATE products SET competitive_price=  " + str(competitive_price)+" where cast(product_id as varchar) = '" + str(product_id) + "'"
        print(sql)
        pgcursor1.execute(sql)
        pgconn.commit()

    else:

        print("competitive price" , competitive_price)
        sql = "UPDATE products SET competitive_price="+  str(competitive_price)+" where cast (product_id as varchar) = '" + str(product_id) + "'"
        print(sql)
        pgcursor1.execute(sql)
        pgconn.commit()

 


    
    
     
    #can_supply_test = fake.boolean(chance_of_getting_true=50)
    
    #sql = "UPDATE responses_from_supplier SET can_supply=  " +  str(can_supply_test) +", offer_price = "+ str(offer_prices) +" where responses_id = '" + response_id + "'"
    #print(sql)
    #pgcursor1.execute(sql)