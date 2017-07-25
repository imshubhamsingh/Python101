import requests

ClientID = "4srCyLEqdCxl0yv0nzElrw"
ClientSecret = "ENSFDsBBTi2MmrRZF10v44yuIrualTSwi5zUNH0W9N5x9PURGOw5lt5ml1LwXob1"

url = "https://api.yelp.com/v3/businesses/search?term=cream+puffs&location=San+Francisco"

r = requests.get(url)

print(r.text)
