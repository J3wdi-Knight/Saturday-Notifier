import requests
import datetime
from location import Location
from notifier import Notifier

class Shabbat:
    def __init__(self):
        self.url = f"https://api.sunrise-sunset.org/json?lat={Location().geoloc[0]}&lng={Location().geoloc[1]}&date=today"
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
                    self.notified = True
                    if self.weekday == 'Friday' and self.get_time_int(self.now) > self.get_time_int(self.dusk):
                        return Notifier.alerm('Shabbat is started', 'Rest')
                        # Here's will be link on notifier module
                    elif self.weekday == 'Saturday' and self.get_time_int(self.now) < self.get_time_int(self.dusk):
                        return Notifier.alerm('Shabbat is going', 'Rest')
                        # Notifier too
                if self.weekday == 'Saturday' and self.get_time_int(self.now) > self.get_time_int(self.dusk):
                    return Notifier.alerm('Shabbat is over', 'Go to work')
        return Notifier.alerm('Not Shabbat', 'Continue to work')
