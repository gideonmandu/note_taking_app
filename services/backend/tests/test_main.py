from test.confest import test_app


client = test_app()


def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "hello, world!"}
