from kafkaconfig import KafkaConfig
from unittest import mock
import os
import pytest


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    patched_environment = {
        "SERVICE_URI": "myurl:9000",
        "SECURITY_PROTOCOL": "PROTOCOL",
        "SSL_CAFILE": "ca.pem",
        "ADMIN_SSL_CERTFILE": "admin.cert",
        "ADMIN_SSL_KEYFILE": "admin.key",
        "USER_SSL_CERTFILE": "user.cert",
        "USER_SSL_KEYFILE": "user.key",
    }

    with mock.patch.dict(os.environ, patched_environment):
        yield


def test_admin_config():
    config = KafkaConfig(admin=True)

    assert config.bootstrap_servers == "myurl:9000"
    assert config.security_protocol == "PROTOCOL"
    assert config.ssl_cafile == "ca.pem"

    assert config.ssl_keyfile == "admin.key"
    assert config.ssl_certfile == "admin.cert"


def test_user_config():
    config = KafkaConfig(admin=False)

    assert config.bootstrap_servers == "myurl:9000"
    assert config.security_protocol == "PROTOCOL"
    assert config.ssl_cafile == "ca.pem"

    assert config.ssl_keyfile == "user.key"
    assert config.ssl_certfile == "user.cert"
