import requests
import datetime
from location import Location
from notifier import Notice, BotSend

class Shabbat:
    def __init__(self):
        self.url = f"https://api.sunrise-sunset.org/json?lat={Location().geoloc[0]}&lng={Location().geoloc[1]}&date=today"
        self.respond = requests.get(self.url)
        self.data = self.respond.json()
        #print(self.data)
        self.today = datetime.date.today()
        self.now = datetime.datetime.now().strftime('%H:%M:%S')
        self.weekday = self.today.strftime('%A')
        self.notified = False

    # Make int from the time [H:M:S PM|AM -> HMS]
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
            self.dusk = self.data.get('results', {}).get('sunset')
            if self.dusk:
                print(self.get_time_int(self.now), self.get_time_int(self.dusk))
                if not self.notified:
                    self.notified = True
                    if self.weekday == 'Friday' and self.get_time_int(self.now) > self.get_time_int(self.dusk):
                        return Notice.alerm('Shabbat is started', 'Rest')
                    elif self.weekday == 'Saturday' and self.get_time_int(self.now) < self.get_time_int(self.dusk):
                        return Notice.alerm('Shabbat is going', 'Rest')
                if self.weekday == 'Saturday' and self.get_time_int(self.now) > self.get_time_int(self.dusk):
                    return Notice.alerm('Shabbat is over', 'Go to work')
        return Notice.alerm('Not Shabbat', 'Continue to work')
