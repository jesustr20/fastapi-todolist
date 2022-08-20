from fastapi.testclient import TestClient
from main import app

def create_user_and_make_login(username: str):
  client = TestClient(app)

  user = {
        'email': f'{username}@cosasdedevs.com',
        'username': username,
        'password': 'admin123'
    }

  response = client.post(
      '/api/v1/user/',
      json=user,
  )

  login = {
      'username': username,
      'password': 'admin123'
  }

  response = client.post(
      '/api/v1/login/',
      data=login,
      headers={
          'Content-Type': 'application/x-www-form-urlencoded'
      },
      allow_redirects=True
  )

  data = response.json()
  return data['access_token']