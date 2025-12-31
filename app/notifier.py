from pathlib import Path
from notifypy import Notify  # pyright: ignore[reportMissingImports]

class Notifier:
    @staticmethod
    def alerm(title=None, message=None) -> None:
        notify = Notify()
        notify.title = title
        notify.message = message

        icon_path = Path('~/Dev/Pet-Projects/python/Shabbat-Notifier/images/Arch_icon.png').expanduser()
        notify.icon = str(icon_path)

        notify.send()
        return
