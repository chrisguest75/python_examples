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


def publisher(topic: str) -> int:
    """publisher function"""
    logger = logging.getLogger()

    logger.info("Posting to Kafka")
    try:
        topic_config = TopicConfig()
        newtopic = Topic(topic_config)
        newtopic.create(topic)

        config = PublisherConfig()
        producer = Publisher(config, topic)
        producer.send()
        del producer
    except Exception as e:
        logger.error(f"Exception: {e}")
        return 1

    return 0


def consumer(topic: str) -> int:
    """publisher function"""
    logger = logging.getLogger()

    logger.info("Receiving from Kafka")
    try:
        topic_config = TopicConfig()
        newtopic = Topic(topic_config)
        newtopic.create(topic)

        consumer_config = ConsumerConfig()
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
    parser.add_argument("--publisher", dest="publisher", action="store_true")
    parser.add_argument("--consumer", dest="consumer", action="store_true")
    parser.add_argument("--topic", dest="topic", type=str, default="default_topic")
    args = parser.parse_args()

    success = 0

    if args.publisher:
        success = publisher(args.topic)
    elif args.consumer:
        success = consumer(args.topic)
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
