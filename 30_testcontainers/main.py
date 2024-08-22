import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
from testcontainers.postgres import PostgresContainer
import psycopg
from customers import customers

def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    """catches unhandled exceptions and logs them"""

    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical(
        "Unhandled Exception {0}: {1}".format(exc_type, exc_value),
        extra={"exception": "".join(traceback.format_tb(exc_traceback))},
    )


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")


def test() -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG={test_config!r}")

    with PostgresContainer("postgres:16", driver=None) as postgres:
        psql_url = postgres.get_connection_url()
        with psycopg.connect(psql_url) as connection:
            with connection.cursor() as cursor:
                version = cursor.execute("SELECT version()").fetchone()
                logger.info(version)

        os.environ["DB_CONN"] = postgres.get_connection_url()
        os.environ["DB_HOST"] = postgres.get_container_host_ip()
        os.environ["DB_PORT"] = postgres.get_exposed_port(5432)
        os.environ["DB_USERNAME"] = postgres.env['POSTGRES_USER']
        os.environ["DB_PASSWORD"] = postgres.env['POSTGRES_PASSWORD']
        os.environ["DB_NAME"] = postgres.env['POSTGRES_DB']
        logger.info(os.environ)

        customers.create_table()
        customers.create_customer("Siva", "siva@gmail.com")
        customers.create_customer("James", "james@gmail.com")
        customers_list = customers.get_all_customers()
        logger.info(len(customers_list))

        customers.create_customer("John", "john@gmail.com")
        customer = customers.get_customer_by_email("john@gmail.com")
        logger.info({'name': customer.name, 'email': customer.email})

    return 0


def main() -> int:
    """
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    """
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="CLI Skeleton")
    parser.add_argument("--test", dest="test", action="store_true")
    args = parser.parse_args()

    success = 0
    if args.test:
        success = test()
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
