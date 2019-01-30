from getpass import getpass
from requests.auth import AuthBase
import requests

# Basic Auth
# response = requests.get('https://api.github.com/user', auth=('kendo1234', getpass()))
# print(response)

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


response = requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))
print(response)