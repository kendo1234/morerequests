import requests
from requests.exceptions import HTTPError


# Checks the response code, basic conditional syntax will pass if response is between 200-400
# Add more specific condition if status is needed
def basic_stuff():
    response = requests.get('https://api.github.com')
    if response:
        print('Success!')

    else:
        print('Not Found.')


# loops through provided URLs and checks HTTP status
def raise_status_error():
    for url in ['https://api.github.com', 'https://api.github.com/invalid']:
        try:
            response = requests.get(url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')


basic_stuff()
raise_status_error()