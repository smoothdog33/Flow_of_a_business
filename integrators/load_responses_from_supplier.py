import json
import os

from connections.connection import get_connection
from faker import Faker
fake = Faker()


                        
                                          


pgcursor,pgconn = get_connection()
def file_inventory_creator(input_directory):
    for root, dirs, files in os.walk(input_directory):
        for file in files:    
            path_creator = os.path.join(root,file)
            file_abs_path = os.path.abspath(path_creator)
            with open(file_abs_path, 'r', encoding='windows-1252') as f:  
                    print(file_abs_path)        
                    for jsonObj in f:
                       product_dictionary = json.loads(jsonObj)
                       supplier_address = (product_dictionary.get('supplier_adress'))
                       supplier_contact = (product_dictionary.get('supplier_contact'))
                       supplier_company = (product_dictionary.get('supplier_company'))
                       supplier_id = (product_dictionary.get('supplier_id'))
                       product_id = (product_dictionary.get('product_id'))
                       product_name = (product_dictionary.get('product_name'))
                       product_discription = (product_dictionary.get('product_discription'))
                       cost = (product_dictionary.get('cost'))
                       price = (product_dictionary.get('price'))
                       question = (product_dictionary.get('question'))                
                       question_id = (product_dictionary.get('question_id'))  
                       sql = "INSERT INTO public.responses_from_supplier(supplier_address, supplier_contact, supplier_company, product_name, product_discription, question, supplier_id, product_id, cost, price, question_id) VALUES ('" + supplier_address + "','" + supplier_contact + "','" + supplier_company + "','" + product_name +"','"+ product_discription +"','" + question +"','"+ str(supplier_id) +"','" + str(product_id)+"','"+ str(cost) + "','" + str(price) + "','"+ str(question_id) + "');"              
                       json_inserter(sql)
                       
                                          

def json_inserter(sql):
    pgconn.autocommit = True
    with pgconn.cursor() as pgcursor:
        pgcursor.execute(sql)
        print (sql)
file_inventory_creator('/Users/ayan/send_to_suppliers/')


                             
                            
        
                                    
                        
