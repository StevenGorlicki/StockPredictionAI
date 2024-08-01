import requests
from requests.auth import HTTPBasicAuth

def main():
    appKey = 'Fq5EQ7kpZI4ZxstIWE8oTuf5lCqAxeu4'
    secretKey = 'Os2Sn5KyQjsdlhMo'
    token_url = 'https://api.schwab.com/oauth/token'

    response = requests.post(token_url, auth=HTTPBasicAuth(appKey, secretKey), data={'grant_type': 'client_credentials'})

    if error_handler(response):
        access_token = response.json()['access_token']
        print('Access Token:', access_token)
        # Use the access token to make an API request
        make_api_request(access_token)
    else:
        print('Failed to get access token.')

def error_handler(response):
    if response.status_code == 200:
        return True
    else:
        print(f'Error: {response.status_code}, {response.text}')
        return False

def make_api_request(access_token):
    api_url = 'https://api.schwab.com/v1/accounts'  # Replace with the actual API endpoint you want to use
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(api_url, headers=headers)

    if error_handler(response):
        data = response.json()
        print('API Response:', data)
    else:
        print('API request failed.')


if __name__ == '__main__':
    main()
