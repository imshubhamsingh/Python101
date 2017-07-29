from requests_oauthlib import OAuth2Session
from pprint import *

ClientID = "4srCyLEqdCxl0yv0nzElrw"
ClientSecret = "ENSFDsBBTi2MmrRZF10v44yuIrualTSwi5zUNH0W9N5x9PURGOw5lt5ml1LwXob1"

yelp = OAuth2Session(client_id=ClientID)
authorization_url, state = yelp.authorization_url('https://api.yelp.com/oauth2/auth')
token = yelp.fetch_token('https://api.yelp.com/oauth2/token', client_secret=ClientSecret,
                         authorization_response=authorization_url, code='yelp', state=state)
print(token)


def do_search(term='Food', location='New York'):
    params = {'location': location,
              'term': term,
              # 'sort_by': 'rating'
              }
    info = yelp.get(url='https://api.yelp.com/v3/businesses/search', params=params)

    return info.json()


search_1 = do_search()

for i in search_1['businesses']:
    print('{name}\n{phone}\n{address}\n{city}\n\n'.format(
        name=i['name'],
        phone=i['phone'],
        address=i['location']['display_address'],
        city=i['location']['city']
    ))

print(len(search_1['businesses']))
