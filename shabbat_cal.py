import requests
import datetime
from location import Location

class Shabbat:
    def __init__(self):
        self.url = f"https://api.sunrisesunset.io/json?lat={Location().geoloc[0]}&lng={Location().geoloc[1]}"
        self.respond = requests.get(self.url)
        self.data = self.respond.json()
        self.today = datetime.date.today()
        self.now = datetime.datetime.now().strftime('%H:%M:%S')
        self.weekday = self.today.strftime('%A')
        self.notified = False

    def get_time_int(self, time: str) -> int:
        self.koef = 0
        if time[-2:] == 'PM':
            self.koef = 12
        self.time = time.replace(':', '')
        self.time = self.time.replace(' AM', '').replace(' PM', '')

        return int(self.time) + (self.koef * 10000)

    @property
    def start(self):
        if self.weekday in ['Friday', 'Saturday']:
            self.dusk = self.data.get('results', {}).get('dusk')
            if self.dusk:
                if not self.notified:
                    if self.weekday == 'Friday' and self.get_time_int(self.now) > self.get_time_int(self.dusk):
                        return 'Shabbat'
                        # Here's will be link on notifier module
                    if self.weekday == 'Saturday' and self.get_time_int(self.now) < self.get_time_int(self.dusk):
                        return 'Shabbat'
                        # Notifier too
                if self.weekday == 'Saturday' and self.get_time_int(self.now) > self.get_time_int(self.dusk):
                    return 'Shabbat is over'
        return 'Not Shabbat'
