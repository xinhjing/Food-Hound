import requests_cache
import requests

# Enable caching
requests_cache.install_cache('yelp_cache', expire_after=3600)

# Set up API request parameters
url = 'https://api.yelp.com/v3/businesses/search'
headers = {
    'Authorization': 'Bearer <API_KEY>',
}
params = {
    'location': 'New York City',
    'categories': 'restaurants',
    'limit': 50,
    'offset': 0,
}

# Make API request
response = requests.get(url, headers=headers, params=params)

# Check if response was served from cache
if response.from_cache:
    print('Response served from cache')
else:
    print('Response served from API')

# Process response data
data = response.json()