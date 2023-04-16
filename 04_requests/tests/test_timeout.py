import timeout


def test_timeout(mocker):
    # Arrange
    expected_data = {"version": "6.3.5"}
    mocked_response = mocker.Mock()
    mocked_response.json.return_value = expected_data

    mock_get = mocker.patch("requests.get", return_value=mocked_response)

    url = "http://0.0.0.0:3001"
    timeout_seconds = 5
    # Act
    response = timeout.timeout_get(url, timeout_seconds)

    # Assert
    mock_get.assert_called_once_with(url, timeout_seconds)
    # assert response["version"] == "6.3.5"
