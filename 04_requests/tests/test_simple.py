import simple

def test_simple():
    response = simple.simple_get("http://0.0.0.0:9001")
    assert response["version"] == "6.3.5"