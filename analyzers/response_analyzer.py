import json
import os
import pandas as pd
import datetime
from datetime import datetime
import psycopg2  
from faker import Faker
fake = Faker()



                                          

try:
    pgcursor,pgconn = get_connection()
except:  
    print('connection is failing')
pgcursor.execute('select can_supply, offer_price from public."responses_from_supplier"')
result = pgcursor.fetchall()     
#supplier_address= result [0][1]


i=1
Faker.seed(0)
for r in result:
    
    can_supply = r[0]
    offer_price = r[1]
   #cost = round(cost,2)
    pgcursor1 = pgconn.cursor()
    if can_supply == 'true':
        for f in offer_price:
            get(smallest)

    else:

        print("  ")

    
     
    #can_supply_test = fake.boolean(chance_of_getting_true=50)
    
    #sql = "UPDATE responses_from_supplier SET can_supply=  " +  str(can_supply_test) +", offer_price = "+ str(offer_prices) +" where responses_id = '" + response_id + "'"
    #print(sql)
    #pgcursor1.execute(sql)