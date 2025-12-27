import requests

# ./app/location - Output the city, country and timezone by ip api

class Location:
    def __init__(self):
        # Get json version of api site
        self.url = 'https://ipinfo.io/json'
        self.respond = requests.get(self.url)
        self.data = self.respond.json()

    # Get city name
    @property
    def city(self):
        return self.data.get('city')

    # Get country name
    @property
    def country(self):
        return self.data.get('country')

    # Get your timezone
    @property
    def timezone(self):
        return self.data.get('timezone')


# That's just for test, right now
locate = Location()
print('city:', locate.city)
print('country:', locate.country)
print('tz:', locate.timezone)
