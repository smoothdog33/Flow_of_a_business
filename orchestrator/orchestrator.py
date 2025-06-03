import multiprocessing
import logging
import json
import os
import threading

from shlex import quote

from pandas.core.common import not_none
from requests.packages import target

# Configure logging
logging.basicConfig(
    level=logging.INFO,              # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    handlers=[
        logging.FileHandler('batch_application.log'),    # Log to a file
        logging.StreamHandler()                          # Log to console
    ]
)
from generators.supplier_profile import supplier_profile_class
from generators.product import product_class
from generators.supplier_questions import supplier_questions_class
from generators.warehouse_profile import warehouse_profile_class
from integrators.supplier_updater import supplier_updater_class
from integrators.supplier_products_questions_xref import supplier_conv_class
from integrators.create_supplier_file_for_quote2 import quote_class
from integrators.load_responses_from_supplier import responses_class
from connections.properties import product_property_func,profile_property_func,questions_property_func,warehouse_property_func,supplier_products_questions_xref,create_supplier_for_quote
from integrators.supplier_updater2 import supplier_updater_class2
from deletion.deletion import file_deletion_func
from deletion.deletion import table_emptier_func

from multiprocessing import Process
from multiprocessing import Pool

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

product_file = product_property_func()
profile_file = profile_property_func()
questions_file = questions_property_func()
warehouse_file = warehouse_property_func()
supplier_products_questions_xref_file = supplier_products_questions_xref()
create_supplier_for_quote_file = create_supplier_for_quote()
print("hi")
import threading

condition = threading.Condition()
completed = set()

def product_orch():
    try:
        error = False
        logging.info("product task started.")
        instance = product_class()
        instance.product_func()
        instance.product_inserter(product_file, 'products')
    except Exception as err:
        logging.info("product task error.")
        logging.info("product task ended.")
        error = (f"Unexpected {err=}, {type(err)=}")
        print(error)
        error = True

    finally:
        if error == False:
            trigger_text = "product generation is finished"
            with open('/inv_mgmt/data/product_trigger.json', 'a') as f:
                json.dump(trigger_text, f)


def profile_orch():
        try:
            logging.info("profile task started.")
            instance1 = supplier_profile_class()
            instance1.supplier_profile()
            instance1.supplier_profile_inserter(profile_file, 'profile_')
        except Exception as err:
            logging.info("profile task error.")
            logging.info("profile task ended.")

        finally:
            trigger_text = "profile generation is finished"
            with open('/inv_mgmt/data/profile_trigger.json', 'a') as f:
                json.dump(trigger_text, f)


def questions_orch():
    try:
        logging.info("questions task started.")
        instance2 = supplier_questions_class()
        instance2.supplier_questions()
        instance2.question_inserter(questions_file, 'questions')
    except Exception as err:
        logging.info("questions task ended.")
        logging.info("questions task ended.")
    finally:
        trigger_text = "questions generation is finished"
        with open('/inv_mgmt/data/questions_trigger.json', 'a') as f:
            json.dump(trigger_text, f)

def warehouse_orch():
        try:
            logging.info("warehouse task started.")
            instance3 = warehouse_profile_class()
            instance3.warehouse_profile()
            instance3.warehouse_inserter(warehouse_file,'warehouse_profile')
        except Exception as err:
            print(f"4Unexpected {err=}, {type(err)=}")
            logging.info("warehouse task error.")
            logging.info("warehouse task ended.")
        finally:
            trigger_text = "warehouse generation is finished"
        with open('/inv_mgmt/data/warehouse_trigger.json', 'a') as f:
            json.dump(trigger_text, f)
def conv_orch():
    if os.path.exists('/inv_mgmt/data/product_trigger.json') and os.path.exists('/inv_mgmt/data/profile_trigger.json') and os.path.exists('/inv_mgmt/data/questions_trigger.json') and os.path.exists('/inv_mgmt/data/warehouse_trigger.json'):
        try:
            logging.info("supplier_conv task started.")
            instance5 = supplier_conv_class()
            instance5.supplier_products_questions_xref_func()
            instance5.supplier_products_questions_xref_inserter(supplier_products_questions_xref(),'supplier_products_questions_xref_table')
        except Exception as err:
            logging.info("supplier_conv task error.")
            logging.info("supplier_conv task ended.")

def supplier_quote_orch():
    try:
        logging.info("supplier quote task started.")
        instance6 = quote_class()
        instance6.quote_select()

    except Exception as err:
        print(f" 5Unexpected {err=}, {type(err)=}")
        logging.info("supplier quote task error.")
        logging.info("supplier quote task ended.")



def responses_orch():
    try:
        logging.info("responses task started.")
        instance7 = responses_class()
        instance7.load_responses(create_supplier_for_quote_file)
        logging.info("responses task ended.")
    except Exception as err:
        print(f"6Unexpected {err=}, {type(err)=}")
        logging.info("responses task error.")
        logging.info("responses task ended.")
def updater_orch():
    try:
        if __name__ == "__main__":
            logging.info("supplier_updater task started.")
            instance8 = supplier_updater_class2()
            #instance8.supplier_updater_func()
           # instance8 = supplier_updater_class()
            instance8.select_func()
    except Exception as err:
        print(f"7Unexpected {err=}, {type(err)=}")
        logging.info("supplier_updater task error.")
        logging.info("supplier_updater task ended.")
def file_deletion_func_thread():
    file_deletion_func()
    with condition:
        completed.add("file")
        condition.notify_all()

def table_emptier_func_thread():
    print("HIIIII")
    table_emptier_func()
    with condition:
        completed.add("table")
        condition.notify_all()

def product_orch_thread():
    print("HIIIII")
    product_orch()
    with condition:
        completed.add("product")
        condition.notify_all()


def profile_orch_thread():
    profile_orch()
    with condition:
        completed.add("profile")
        condition.notify_all()

def questions_orch_thread():
    questions_orch()
    with condition:
        completed.add("questions")
        condition.notify_all()

def warehouse_orch_thread():
    warehouse_orch()
    with condition:
        completed.add("warehouse")
        condition.notify_all()

def conv_orch_thread():
    with condition:
        while not {"product", "profile", "questions", "warehouse"}.issubset(completed):
            condition.wait()
    conv_orch()
    with condition:
        completed.add("conv")
        condition.notify_all()
def supplier_quote_orch_thread():
    print("Supplier quote thread started")
    with condition:
        while "conv" not in completed:
            condition.wait()
    supplier_quote_orch()
    with condition:
        completed.add("quote")
        condition.notify_all()
def responses_orch_thread():
    print("responses orch thread started")
    with condition:
        while "quote" not in completed:
            condition.wait()
    responses_orch()
    with condition:
        completed.add("response")
        condition.notify_all()


# Start threads

if __name__ == "__main__":
    threads = [

        threading.Thread(target=file_deletion_func_thread),
        threading.Thread(target=table_emptier_func_thread),
        threading.Thread(target=product_orch_thread),
        threading.Thread(target=profile_orch_thread),
        threading.Thread(target=questions_orch_thread),
        threading.Thread(target=warehouse_orch_thread),
        threading.Thread(target=conv_orch_thread),
        threading.Thread(target=supplier_quote_orch_thread),
        threading.Thread(target=responses_orch_thread)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()