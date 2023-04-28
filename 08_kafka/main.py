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
from topic import Topic, TopicConfig


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


def str2bool(v) -> bool:
    """ converts strings representing truth to bool """ ""
    return v.lower() in ("yes", "true", "t", "1")


def publisher(topic: str, admin: bool, create: bool, repeat: int) -> int:
    """publisher function"""
    logger = logging.getLogger()

    try:
        if create:
            logger.info("Create topic")
            topic_config = TopicConfig(admin=admin)
            newtopic = Topic(topic_config)
            newtopic.create(topic)

        logger.info("Posting to Kafka")
        config = PublisherConfig(admin=admin)
        producer = Publisher(config, topic)
        producer.send(repeat=repeat)
        del producer
    except Exception as e:
        logger.error(f"Exception: {e}")
        return 1

    return 0


def consumer(topic: str, admin: bool, create: bool) -> int:
    """publisher function"""
    logger = logging.getLogger()

    try:
        if create:
            logger.info("Create topic")
            topic_config = TopicConfig(admin=admin)
            newtopic = Topic(topic_config)
            newtopic.create(topic)

        logger.info("Receiving from Kafka")
        consumer_config = ConsumerConfig(admin=admin)
        consumer = Consumer(consumer_config, topic)
        consumer.receive()
        del consumer
    except Exception as e:
        logger.error(f"Exception: {e}")
        return 1

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

    parser = argparse.ArgumentParser(description="Kafka Example")
    parser.add_argument("--admin", dest="admin", action="store_true")
    parser.add_argument("--publisher", dest="publisher", action="store_true")
    parser.add_argument("--consumer", dest="consumer", action="store_true")
    parser.add_argument("--create", dest="create", action="store_true")
    parser.add_argument("--topic", dest="topic", type=str, default="default_topic")
    parser.add_argument("--repeat", dest="repeat", type=int, default=10)
    args = parser.parse_args()

    success = 0

    if args.publisher:
        success = publisher(args.topic, args.admin, args.create, args.repeat)
    elif args.consumer:
        success = consumer(args.topic, args.admin, args.create)
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
