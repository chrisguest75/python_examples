import simple


def test_simple(mocker):
    # Arrange
    expected_data = {"version": "6.3.5"}
    mocked_response = mocker.Mock()
    mocked_response.json.return_value = expected_data

    mock_get = mocker.patch("requests.get", return_value=mocked_response)

    url = "http://0.0.0.0:3001"

    # Act
    response = simple.simple_get(url)

    # Assert
    mock_get.assert_called_once_with(url)
    assert response["version"] == "6.3.5"
