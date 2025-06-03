import platform
import threading

#from analyzers.response_analyzer import can_supply
from generators.supplier_profile import supplier_profile_class
from generators.product import product_class
from generators.supplier_questions import supplier_questions_class
from generators.warehouse_profile import warehouse_profile_class
from integrators.supplier_updater2 import supplier_updater_class
from integrators.supplier_updater2 import supplier_updater_class

from integrators.supplier_convert2 import supplier_conv_class
from connections.connection import get_connection

import pandas
import argparse
from faker import Faker
fake = Faker()
#instance = product_class()
#instance1 = supplier_profile_class()
#instance2 = supplier_questions_class()
#instance3 = warehouse_profile_class()
#instance4 = supplier_updater_class()
#instance5 = supplier_conv_class()

try:
    print("PRoduct")
    instance = product_class()
    instance.product_func()
    instance.product_inserter('/Users/ayanbhatt/IdeaProjects/Inv_managment/target_project/data/product.json', 'products')

except Exception as err:
    print(f"1Unexpected {err=}, {type(err)=}")

try:
    instance1 = supplier_profile_class()
    instance1.supplier_profile()
    instance1.supplier_profile_inserter('/Users/ayanbhatt/IdeaProjects/Inv_managment/target_project/data/supplier_profile1.json', 'profile_')
    print("Supp Profile")
except Exception as err:
    print(f"2Unexpected {err=}, {type(err)=}")

try:
    instance2 = supplier_questions_class()
    instance2.supplier_questions()
    instance2.question_inserter('/Users/ayanbhatt/IdeaProjects/Inv_managment/target_project/data/questions.json', 'questions')
    print("supplier_questions_class")
except Exception as err:
    print(f"3Unexpected {err=}, {type(err)=}")

try:
   instance3 = warehouse_profile_class()
   instance3.warehouse_profile()
   instance3.warehouse_inserter('/Users/ayanbhatt/IdeaProjects/Inv_managment/target_project/data/warehouse_profile.json','warehouse_profile')
except Exception as err:
    print(f"4Unexpected {err=}, {type(err)=}")



try:
    instance5 = supplier_conv_class()
    instance5.supplier_conv()
    instance5.convert_inserter('/Users/ayanbhatt/IdeaProjects/Inv_managment/target_project/data/supplier_conv.json','convert_')
except Exception as err:
    print(f"6Unexpected {err=}, {type(err)=}")
try:
    print("supplier updater")
    instance4 = supplier_updater_class()
    instance4.select_func()
   # can_supply_test = instance4.can_supply_test
   # instance4.update_func(can_supply_test,offer_prices,response_id,pgcursor2,pgconn)
except Exception as err:
    print(f"5Unexpected {err=}, {type(err)=}")

