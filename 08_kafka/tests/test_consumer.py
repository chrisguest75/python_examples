from consumer import Consumer, ConsumerConfig
import json
import logging
import unittest
from unittest.mock import MagicMock, Mock, patch


class MockedConsumer(Consumer):
    def __init__(self, config, topic):
        super().__init__(config, topic)
        self.consumer = MagicMock()


def test_check_messages_successful():
    consumer_config = ConsumerConfig(admin=True)
    consumer = MockedConsumer(consumer_config, "test_topic")

    consumer.consumer.subscribe = MagicMock()
    consumer.logger.info = MagicMock()

    mock_messages = [
        Mock(value=json.dumps({"msg": "Test message 1"}).encode("utf-8")),
        Mock(value=json.dumps({"msg": "Test message 2"}).encode("utf-8")),
    ]
    consumer.consumer.__iter__.return_value = iter(mock_messages)

    with patch("logging.info") as mock_logging_info, patch(
        "logging.error"
    ) as mock_logging_error:
        consumer.check_messages()

        consumer.consumer.subscribe.assert_called_once_with([consumer.TOPIC_NAME])
        assert consumer.logger.info.call_count == 2


def test_check_messages_with_errors():
    consumer_config = ConsumerConfig(admin=True)
    consumer = MockedConsumer(consumer_config, "test_topic")

    consumer.consumer.subscribe = MagicMock()
    consumer.logger.info = MagicMock()
    consumer.logger.error = MagicMock()

    mock_messages = [
        Mock(value=json.dumps({"msg": "Test message 1"}).encode("utf-8")),
        Mock(value="malformed_message".encode("utf-8")),
    ]
    consumer.consumer.__iter__.return_value = iter(mock_messages)

    with patch("logging.info") as mock_logging_info, patch(
        "logging.error"
    ) as mock_logging_error:
        consumer.check_messages()

        consumer.consumer.subscribe.assert_called_once_with([consumer.TOPIC_NAME])
        assert consumer.logger.info.call_count == 1
        assert consumer.logger.error.call_count == 1
