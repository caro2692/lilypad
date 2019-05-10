import requests

TIDEPOOL_USER_ID = '31366224c0'
TIDEPOOL_SESSION_ID = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkdXIiOjI1OTIwMDAsImV4cCI6MTU1OTY3MzE5MSwic3ZyIjoibm8iLCJ1c3IiOiIzMTM2NjIyNGMwIn0.KAKdlTW-ojjN7xB9MbcZqwHkui1JtJ3cVM0PPfENRKE'


def get_user_data():
    base_url = 'https://int-api.tidepool.org/metadata/users/'
    url = base_url + TIDEPOOL_USER_ID + '/users'
    headers = {'x-tidepool-session-token': TIDEPOOL_SESSION_ID}

    response = requests.get(url, params={}, headers=headers)

    return response
