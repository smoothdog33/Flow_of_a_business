from future.backports.datetime import datetime
from sqlalchemy.sql.functions import current_timestamp

try:
    from connections.connection import get_connection
except ImportError:
    print("import error")

from faker import Faker
fake = Faker()
class supplier_updater_class():
    def supplier_updater_func():
        try:
            pgcursor,pgconn = get_connection()
        except:
            print('connection is failing')
        pgcursor.execute('select responses_id, price from public."responses_from_supplier"')
        result = pgcursor.fetchall()


        i=1
        Faker.seed(0)
        print (datetime.now())
        for r in result:

            price = r[1]
            response_id = r[0]
            #print(response_id)
            pgcursor1 = pgconn.cursor()
            try:
                offer_prices =  float(price)  * float((fake.pydecimal(max_value=1, min_value=0.5)))
            except ArithmeticError:
                print("something is wrong with the math, there was an arithmitic error")
            responses_ids = fake.pystr(5)

            can_supply_test = fake.boolean(chance_of_getting_true=50)

            sql = "UPDATE responses_from_supplier SET can_supply=  " +  str(can_supply_test) +", offer_price = "+ str(offer_prices) +" where responses_id = " + "'" + str(response_id) + "'"
            #+ ", offer_price= " + str(offer_prices)+ ", responses_id =" + (responses_ids)
            #print(sql)
            pgcursor1.execute(sql)
            pgconn.commit()
        print(datetime.now())

supplier_updater_class.supplier_updater_func()