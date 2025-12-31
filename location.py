import requests

class Location:
    def __init__(self) -> None:
        # Get json version of api site
        self.url = 'https://ipinfo.io/json'
        self.respond = requests.get(self.url)
        self.data = self.respond.json()

    @property
    def city(self) -> str:
        return self.data.get('city')

    @property
    def country(self) -> str:
        return self.data.get('country')

    @property
    def geoloc(self) -> list:
        # Split str;    list[lat, lng]
        self.loc = self.data.get('loc').split(',')
        return self.loc

    @property
    def timezone(self) -> str:
        return self.data.get('timezone')
