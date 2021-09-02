from tests.confest import test_app


def test_home(test_app):
    response = test_app.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "hello, world!"}
