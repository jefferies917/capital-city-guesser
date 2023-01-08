import requests


def test_index():
    response = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
    assert response.status_code == 200

    response_body = response.json()
    assert response_body['data'][0]['name'] == 'Afghanistan'