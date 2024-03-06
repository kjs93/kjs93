import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

access_key = "Fvlj2ibYwAZxXU3Gw1xDQQYhYxfy7nTlFxmxW9uN"
secret_key = "1J0oPxFXtoAGH8YeXU9IjVL3a9XOIanxbQmIxxFc"

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.get("https://api.upbit.com/v1/accounts", headers=headers)
res.json()
print(res.json()[1]['balance'])