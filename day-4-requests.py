
import requests

#  the link we will get the data
url = 'https://api.github.com/users/MahmoudFathyTawfeek'

# send request
response = requests.get(url)

# print data and status code
print(f"Status Code: {response.status_code}")
print("--- Response Content (JSON) ---")
print(response.json()) # convert the response to dictionary