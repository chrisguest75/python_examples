from main import start_monitor
from unittest import mock
import io
import json
from unittest.mock import MagicMock, patch
from interval import Interval


def test_monitor_disabled():
    mock_file_content = {
        "sites": {
            "podinfo_root": {
                "enabled": False,
                "verb": "GET",
                "url": "http://0.0.0.0:9001",
                "timeoutMs": 2000,
                "regex": "hostname",
                "intervalMs": 10000,
                "follow_redirects": True,
                "check_certificate_expiration": False,
                "verify_ssl": True,
                "tags": {"env": "prod"},
            }
        }
    }
    with patch("interval.Interval") as MockInterval:
        mock_interval_instance = MockInterval.return_value
        mock_interval_instance.start = MagicMock()
        start_monitor(mock_file_content)

        assert mock_interval_instance.start.call_count == 0


# def test_monitor_enabled():
#     mock_file_content = {
#         "sites": {
#             "podinfo_root": {
#                 "enabled": True,
#                 "verb": "GET",
#                 "url": "http://0.0.0.0:9001",
#                 "timeoutMs": 2000,
#                 "regex": "hostname",
#                 "intervalMs": 10000,
#                 "follow_redirects": True,
#                 "check_certificate_expiration": False,
#                 "verify_ssl": True,
#                 "tags": {"env": "prod"},
#             }
#         }
#     }
#     with patch("interval.Interval") as MockInterval:
#         mock_interval_instance = MockInterval.return_value
#         mock_interval_instance.start = MagicMock()
#         start_monitor(mock_file_content)

#         assert mock_interval_instance.start.call_count == 1
