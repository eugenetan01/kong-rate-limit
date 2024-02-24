import requests

# The URL of the endpoint you want to hit
url = "http://localhost:8000/mock"

# Number of times you want to hit the endpoint
num_requests = 6

for i in range(num_requests):
    # Sending a GET request to the URL
    response = requests.get(url)

    # Printing the status code to see if the request was successful
    print(f"Request #{i+1}: Status Code = {response.status_code} ")

    # Printing the error message if the status code is not 200
    if response.status_code != 200:
        print(f"Error message: {response.text}")
