import platform
from supplier_convert2 import json_inserter

import pandas
import argparse
from connections.connection import get_connection
from faker import Faker
fake = Faker()


                        
                                          


try:
    pgcursor,pgconn = get_connection()  
except:  
    print('connection is failing')

pd = pandas
parser = argparse.ArgumentParser()
args = parser.parse_args()
g = (platform.uname())
source_system_id = g[0]+" "+ g[1]
print (source_system_id)

#supplier_conv()
#product_func()
json_inserter('supplier_conv.json','convert_') 
#supplier_profile()

#json_inserter('supplier_profile.json','profile_') 

#supplier_questions()

#json_inserter('warehouse_profile.json','warehouse_profile')

