import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
from publisher import Publisher, PublisherConfig
from consumer import Consumer, ConsumerConfig


def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    ''' catches unhandled exceptions and logs them '''

    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical(
        "Unhandled Exception {0}: {1}".format(exc_type, exc_value),
        extra={"exception": "".join(traceback.format_tb(exc_traceback))},
    )


def str2bool(v) -> bool:
    ''' converts strings representing truth to bool '''''
    return v.lower() in ("yes", "true", "t", "1")


def publisher() -> int:
    ''' publisher function '''
    logger = logging.getLogger()

    logger.info("Posting to Kafka")
    try:
        config = PublisherConfig()
        producer = Publisher(config)
        producer.send()
        del producer
    except Exception as e:
        logger.error(f"Exception: {e}")
        return 1

    return 0

def consumer() -> int:
    ''' publisher function '''
    logger = logging.getLogger()

    logger.info("Receiving from Kafka")
    try:
        config = ConsumerConfig()
        consumer = Consumer(config)
        consumer.receive()
        del consumer
    except Exception as e:
        logger.error(f"Exception: {e}")
        return 1

    return 0


def main() -> int:
    '''
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    '''
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="Kafka Example")
    parser.add_argument("--publisher", dest="publisher", action="store_true")
    parser.add_argument("--consumer", dest="consumer", action="store_true")
    args = parser.parse_args()

    success = 0
    if args.publisher:
        success = publisher()
    elif args.consumer:
        success = consumer()
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
