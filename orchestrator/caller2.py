import platform

from generators.supplier_profile import supplier_profile_class

from generators.product import product_class
from generators.supplier_questions import supplier_questions_class

from generators.warehouse_profile import warehouse_profile_class

from integrators.supplier_updater import supplier_updater_class

from integrators.supplier_convert2 import supplier_conv_class

from connections.connection import get_connection


import pandas
import argparse
from faker import Faker
fake = Faker()
instance = product_class()
instance1 = supplier_profile_class()
instance2 = supplier_questions_class()
instance3 = warehouse_profile_class()
instance4 = supplier_updater_class()
instance5 = supplier_conv_class()

try:
    instance.product_func()
    instance.product_inserter('/Users/ayan/IdeaProjects/target/data/product.json', 'products')
except Exception as err:
    print(f"1Unexpected {err=}, {type(err)=}")

try:

    instance1.supplier_profile()
    instance1.supplier_profile_inserter('/Users/ayan/IdeaProjects/target/data/supplier_profile1.json', 'profile_')

except Exception as err:
    print(f"2Unexpected {err=}, {type(err)=}")

try:
    instance2.supplier_questions()
    instance2.question_inserter('/Users/ayan/IdeaProjects/target/data/questions.json', 'questions')
except Exception as err:
    print(f"3Unexpected {err=}, {type(err)=}")

try:
    instance3.warehouse_profile()
    instance3.warehouse_inserter('/Users/ayan/IdeaProjects/target/data/warehouse_profile.json','warehouse_profile')
except Exception as err:
    print(f"4Unexpected {err=}, {type(err)=}")

try:
    instance5.supplier_conv()
    instance5.convert_inserter('/Users/ayan/IdeaProjects/target/data/supplier_conv.json','convert_')
except Exception as err:
    print(f"5Unexpected {err=}, {type(err)=}")

try:
    instance6.

'''
try:
    instance4.supplier_updater_func()
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
 
'''

pd = pandas
parser = argparse.ArgumentParser()
args = parser.parse_args()
g = (platform.uname())
source_system_id = g[0]+" "+ g[1]
print (source_system_id)

#supplier_conv()
#product_func()
#json_inserter('../integrators/supplier_conv.json', 'convert_')
#supplier_profile()

#json_inserter('supplier_profile.json','profile_') 

#supplier_questions()

#json_inserter('warehouse_profile.json','warehouse_profile')

