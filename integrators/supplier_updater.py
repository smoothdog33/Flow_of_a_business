try:
    from connections.connection import get_connection
except ImportError:
    print("import error")

from faker import Faker
fake = Faker()
class supplier_updater_class():
    def supplier_updater_func(self):
        try:
            pgcursor,pgconn = get_connection()
        except:
            print('connection is failing')
        pgcursor.execute('select responses_id, price from public."responses_from_supplier"')
        result = pgcursor.fetchall()
        print(result.count(1))

        i=1
        Faker.seed(0)
        for r in result:

            price = r[1]
            response_id = r[0]
            pgcursor1 = pgconn.cursor()
            try:
                offer_prices =  price  * float((fake.pydecimal(max_value=1, min_value=0.5)))
            except ArithmeticError:
                print("something is wrong with the math, there was an arithmitic error")
            responses_ids = fake.pystr(5)

            can_supply_test = fake.boolean(chance_of_getting_true=50)

            sql = "UPDATE responses_from_supplier SET can_supply=  " +  str(can_supply_test) +", offer_price = "+ str(offer_prices) +" where responses_id = '" + response_id + "' and question_id = 153"
            #+ ", offer_price= " + str(offer_prices)+ ", responses_id =" + (responses_ids)
            print(sql)
            pgcursor1.execute(sql)
            pgconn.commit()
            print('worked')


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
        # and do the flow charrt of this project





