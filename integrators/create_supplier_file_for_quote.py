import connections
import pandas

import json
pd = pandas


from faker import Faker
fake = Faker()


                        
                                          


try:
    pgcursor,pgconn = connections.get_connection()
except:
    print('connection is failing')


def json_inserter():
        
        
        postgreSQL_select_Query = "select * from profile_"
        pgcursor.execute(postgreSQL_select_Query)
        profile_records = pgcursor.fetchall()
        for row in profile_records:
            print("Id = ", row[0], )
            print("Model = ", row[1])
            print("Price  = ", row[2])
            print("Supplier_id  = ", row[3], "\n")
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
                with open('/Users/ayan/send_to_suppliers/'+'supplier_'+ supplier_company + '.json', 'a') as f:
                    c = {"supplier_adress": supplier_address,"supplier_contact": supplier_contact,"supplier_company":supplier_company,"supplier_id": supplier_id,"supplier_email":supplier_email,"product_id":product_id,"product_name":product_name,"product_discription":product_discription,"cost":cost,"price":price,"question":question,"question_id":question_id} 
                with open('/Users/ayan/send_to_suppliers/'+'supplier_'+ supplier_company + '.json', 'a') as f:     
                            json.dump(c, f)
                            f.write('\n') 


json_inserter()