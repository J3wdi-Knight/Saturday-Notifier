from pathlib import Path
from notifypy import Notify
import bot

class Notice:
    @staticmethod
    def alerm(title=None, message=None) -> None:
        notify = Notify()
        notify.title = title
        notify.message = message

        icon_path = Path('~/Dev/Pet-Projects/python/Shabbat-Notifier/images/Arch_icon.png').expanduser()
        notify.icon = str(icon_path)

        notify.send()
        return

class Mail:
    @staticmethod
    def alerm():
        pass

class BotSend:
    @staticmethod
    def alerm():
        return bot()  # pyright: ignore[reportCallIssue]
