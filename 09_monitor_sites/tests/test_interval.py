import pytest

from main import start_monitor
from unittest import mock
import os
import json
from unittest.mock import MagicMock, patch
from endpoint import Endpoint
from interval import Interval
import requests


def test_interval_extracthostname():
    hostname = Interval.extract_hostname("https://www.google.com")
    assert hostname == "www.google.com"


def test_interval_extracthostname_with_port():
    hostname = Interval.extract_hostname("https://www.google.com:9000")
    assert hostname == "www.google.com"


def test_interval_extracthostname_with_port_root():
    hostname = Interval.extract_hostname("https://www.google.com:9000/")
    assert hostname == "www.google.com"


def test_interval_extracthostname_with_port_route():
    hostname = Interval.extract_hostname("https://www.google.com:9000/root")
    assert hostname == "www.google.com"


def test_interval_extracthostname_with_port_route_query():
    hostname = Interval.extract_hostname("https://www.google.com:9000/root?query=1")
    assert hostname == "www.google.com"


@pytest.fixture
def endpoint():
    return Endpoint(
        name="podinfo_root",
        enabled=True,
        verb="GET",
        url="https://www.google.com",
        timeoutMs=2000,
        regex="hostname",
        intervalMs=10000,
        follow_redirects=True,
        check_certificate_expiration=False,
        verify_ssl=True,
        tags={"env": "prod"},
    )


@pytest.fixture
def interval(endpoint):
    return Interval(endpoint=endpoint)


def test_matcher_with_match(interval):
    response = "hostname: podinfo-5f7b4f5f4f-4q9q2"
    result = interval.matcher(response=response, regex="hostname")
    assert result is True


def test_matcher_with_no_match(interval):
    response = "host: podinfo-5f7b4f5f4f-4q9q2"
    result = interval.matcher(response=response, regex="hostname")
    assert result is False


def test_interval_stop_without_start(interval):
    interval.stop()


def test_interval_start(interval):
    interval.matcher = MagicMock()
    interval.logger.info = MagicMock()
    interval.logger.error = MagicMock()
    # Mock the perf_counter function
    mock_perf_counter = MagicMock()
    mock_perf_counter.side_effect = [1.0, 2.0]
    mock_time = MagicMock(return_value=1234567890)

    with patch("logging.info") as mock_logging_info, patch(
        "logging.error"
    ) as mock_logging_error, patch("threading.Timer") as MockTimer, patch(
        "requests.get"
    ) as mock_get, patch(
        "time.perf_counter", mock_perf_counter
    ), patch(
        "time.time", mock_time
    ):
        response = interval.ping()

        mock_get.assert_called_once_with("https://www.google.com", timeout=2)
        assert mock_perf_counter.call_count == 2
        assert response.elapsedMs == 1000.0
        assert response.timestamp == 1234567890
        assert response.name == "podinfo_root"
        assert response.expiry_date == "UNCHECKED"
        assert response.verb == "GET"
        assert response.url == "https://www.google.com"
