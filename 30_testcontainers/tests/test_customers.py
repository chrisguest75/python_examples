import os
import pytest
from testcontainers.postgres import PostgresContainer
from customers import customers
import psycopg
import time

@pytest.fixture(scope="module", autouse=True)
def setup(request):
    postgres = PostgresContainer("postgres:16-alpine", driver=None)
    postgres.start()
    # psql_url = postgres.get_connection_url()
    # with psycopg.connect(psql_url) as connection:
    #     with connection.cursor() as cursor:
    #         version = cursor.execute("SELECT version()").fetchone()
    #         print(version)

    def remove_container():
        postgres.stop()

    request.addfinalizer(remove_container)
    #time.sleep(10) 

    os.environ["DB_CONN"] = postgres.get_connection_url()
    os.environ["DB_HOST"] = postgres.get_container_host_ip()
    os.environ["DB_PORT"] = postgres.get_exposed_port(5432)
    os.environ["DB_USERNAME"] = postgres.env['POSTGRES_USER']
    os.environ["DB_PASSWORD"] = postgres.env['POSTGRES_PASSWORD']
    os.environ["DB_NAME"] = postgres.env['POSTGRES_DB']
    print(os.environ)
    customers.create_table()
    return postgres

@pytest.fixture(scope="function", autouse=True)
def setup_data():
    customers.delete_all_customers()

def test_get_all_customers():
    customers.create_customer("Siva", "siva@gmail.com")
    customers.create_customer("James", "james@gmail.com")
    customers_list = customers.get_all_customers()
    assert len(customers_list) == 2


def test_get_customer_by_email():
    customers.create_customer("John", "john@gmail.com")
    customer = customers.get_customer_by_email("john@gmail.com")
    assert customer.name == "John"
    assert customer.email == "john@gmail.com"

