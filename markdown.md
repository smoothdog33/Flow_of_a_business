Data Pipeline Project
OOP through Classes and Functions

The project uses object-oriented programming to separate logic into different modules. For example, in the Generator module, there are classes like SupplierGenerator, ProductGenerator, and QuestionGenerator. These classes have functions like generate_supplier_data() or generate_product_data() that create the fake data and move it through the pipeline. In the Processor module, we have classes like SupplierUpdater that take generated data and update the database. This design keeps the code modular, reusable, and easy to maintain.

Organization of Classes, Functions, and Python Files

The code is split into multiple files, each focused on a single responsibility.

Generator files → create supplier, product, and question data.

delete.py → cleans up files and tables.

orchestrator.py → runs the entire flow in the correct sequence.

This structure makes it easy to replace or change one part without affecting other parts of the system.

Proper Error Handling

Different types of operations have their own try-except blocks:

Database connections → catch psycopg2.DatabaseError

File operations → catch IOError

JSON parsing → catch ValueError

We also use finally blocks to ensure connections are always closed properly, which prevents resource leaks and keeps the system stable.

Logging

The system uses Python’s built-in logging module.

INFO logs → track normal runs (e.g., when suppliers are generated or data is compiled).

ERROR logs → capture failures or exceptions.

This creates a clear record of what happened, where, and why, which is helpful for debugging and monitoring production runs.

Orchestration

The orchestrator module controls the overall pipeline:

Sequences dependent tasks (e.g., products must be generated before product-question mappings).

Runs independent tasks (like supplier generation and warehouse generation) in parallel using Python’s multiprocessing module.

This orchestration ensures efficiency and correctness across the workflow.

Dependency Sequencing, Parallelizing, Conditional Processing, Scheduling

Sequenced tasks → Supplier → Product → Question (must run in order).

Parallel tasks → Supplier generation and Warehouse generation (run independently).

Conditional tasks → Some modules (like deletion) are skipped based on config values.

The orchestrator manages this pipeline to balance speed and accuracy.

Config-Based Systematic Runs

All important settings are stored in config files, including:

Database connections

File paths and output filenames

Number of records to generate

Scheduling rules

By keeping configs separate from logic, the pipeline is easily reusable across environments and adaptable to different datasets.

Maintaining Data and Referential Integrity

Suppliers, products, and questions are cross-linked. The pipeline ensures:

Every product maps to a valid supplier.

Product-question mappings reference existing products and questions.

This guarantees data accuracy across the database even with large-scale generation and updates.

Relational Database Modeling

The PostgreSQL database uses normalized tables for suppliers, products, questions, responses, and cross-references. Relationships are enforced through primary keys and foreign keys, which ensures referential integrity. This design supports fast joins, scalable querying, and long-term flexibility.

Docker Integration

The entire pipeline runs inside Docker containers, which makes it portable and consistent across environments.

PostgreSQL runs in one container for database storage.

The pipeline modules (generators, processors, orchestrators) run in separate containers.

Kafka is containerized to handle real-time message passing between modules.

This setup ensures reproducibility, easy deployment, and smooth collaboration.
