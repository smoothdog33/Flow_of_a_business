import os

# Get the environment variable 'ENV', default to 'local' if not set
env = os.getenv('ENV', 'local').lower()

if env == "docker":
        base_data_directory = "/inv_mgmt/data/"
        supplier_data_directory =  "/inv_mgmt/"
        def docker_test():
            return 1
        docker_test()
else:

        base_data_directory = "/Users/ayanbhatt/Documents/inv_mgmt/data/"



def product_property_func():
    return os.path.join(base_data_directory, 'product.json')

def profile_property_func():
    return os.path.join(base_data_directory, 'supplier_profile1.json')

def questions_property_func():
    return os.path.join(base_data_directory, 'questions.json')

def warehouse_property_func():
    # Assuming warehouse data is in a different path even locally
    if env == "docker":
        return "/inv_mgmt/warehouse_profile.json"  # example docker path
    else:
        return "/Users/ayanbhatt/IdeaProjects/Inv_managment/target_project/data/warehouse_profile.json"

def load_responses():
    return os.path.join(supplier_data_directory, 'send_to_suppliers', 'send_to_suppliers.json')

def supplier_products_questions_xref():
    return os.path.join(base_data_directory, 'supplier_conv.json')

def create_supplier_for_quote():
    a = os.path.join(supplier_data_directory, 'send_to_suppliers')

    print(a)
    return os.path.join(supplier_data_directory, 'send_to_suppliers')


def counts_of_generations():
    product_count = 5
    question_count = 2
    supplier_profile_count = 5
    warehouse_profile_count = 5
    gent_counts = [product_count, question_count, supplier_profile_count, warehouse_profile_count]
    return gent_counts

# For debugging: print which environment and base directory is used
if __name__ == "__main__":
    print(f"Running in environment: {env}")
    print(f"Using base data directory: {base_data_directory}")
    print(f"Product JSON path: {product_property_func()}")
