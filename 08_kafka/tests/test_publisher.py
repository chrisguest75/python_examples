from publisher import Publisher, PublisherConfig
import json
import logging
import unittest
from unittest.mock import MagicMock, Mock, patch


class MockedPublisher(Publisher):
    def __init__(self, config, topic):
        super().__init__(config, topic)
        self.publisher = MagicMock()


def test_send_message():
    publisher_config = PublisherConfig(admin=True)
    publisher = MockedPublisher(publisher_config, "test_topic")

    publisher.producer.send = MagicMock()
    publisher.logger.info = MagicMock()
    publisher.logger.error = MagicMock()

    mock_message = {"msg": "Test message 1"}

    with patch("logging.info") as mock_logging_info, patch(
        "logging.error"
    ) as mock_logging_error:
        publisher.send_message(mock_message)

        # Pass the correct arguments to the `assert_called_once_with` method
        encoded_message = json.dumps(mock_message).encode("utf-8")
        publisher.producer.send.assert_called_once_with(
            publisher.TOPIC_NAME, encoded_message
        )

        assert publisher.logger.info.call_count == 1
