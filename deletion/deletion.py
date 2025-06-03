import os

from connections.connection import get_connection

try:
    pgcursor, pgconn = get_connection()
except:
    print('connection is failing')
def file_deletion_func():
    directory = '/inv_mgmt/data/'
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        os.remove(file_path)
    directory = '/inv_mgmt/send_to_suppliers'
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        os.remove(file_path)
file_deletion_func()

def table_emptier_func():
    pgcursor, pgconn = get_connection()

    sql = "delete from supplier_products_questions_xref_table; delete from products;delete from profile_;delete from questions;delete from responses_from_supplier;delete from warehouse_profile"
    print("now i am connecting to pg")
    pgconn.autocommit = True
    print("now i am connected to pg")
    with pgconn.cursor() as pgcursor:
        print("now i am trying to insert data")
        print(sql)
        pgcursor.execute(sql)
table_emptier_func()


''''
import os
def file_deletion_func():
    directory = '/Users/ayanbhatt/IdeaProjects/target_project/data'

    # Remove all files in the directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    if os.path.exists("/Users/ayanbhatt/IdeaProjects/target_project/data/product.json"):
        os.remove("/Users/ayanbhatt/IdeaProjects/target_project/data/product.json")
    else:
        print("no product json")
    if os.path.exists("/Users/ayanbhatt/IdeaProjects/target_project/data/supplier_profile1.json"):
        os.remove("/Users/ayanbhatt/IdeaProjects/target_project/data/supplier_profile1.json")
    else:
        print("no supplier profile json")
    if os.path.exists("/Users/ayanbhatt/IdeaProjects/target_project/data/questions.json"):
        os.remove("/Users/ayanbhatt/IdeaProjects/target_project/data/questions.json")
    else:
        print("no supplier questions json")
    if os.path.exists("/Users/ayanbhatt/IdeaProjects/target_project/data/warehouse_profile.json"):
        os.remove("/Users/ayanbhatt/IdeaProjects/target_project/data/warehouse_profile.json")
    else:
        print("no warehouse profile json")
    if os.path.exists("/Users/ayanbhatt/IdeaProjects/target_project/data/supplier_conv.json"):
        os.remove("/Users/ayanbhatt/IdeaProjects/target_project/data/supplier_conv.json")
    else:
        print("no supplier_conv  json")


file_deletion_func()

'''