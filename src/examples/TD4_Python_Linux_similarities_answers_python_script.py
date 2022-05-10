import requests

uri = 'https://opendomesday.org/api/1.0/county/'
target = 'Derbyshire'

r = requests.get(uri)
counties = r.json()
county_info = next(c for c in counties if c['name'] == target)
place_ids = [p['id'] for p in county_info['places_in_county']]
print(place_ids)

