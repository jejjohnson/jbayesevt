from dataclasses import dataclass
import datetime

@dataclass
class Time:
    datetime: datetime.datetime

    def __init__(self, *args, **kwargs):
        self.datetime = datetime.datetime(*args, **kwargs)

    @property
    def date(self):
        return str(self.datetime.date())

    @property
    def year(self):
        return self.datetime.strftime("%Y")

    @property
    def month(self):
        return self.datetime.strftime("%m")

    @property
    def day(self):
        return self.datetime.strftime("%d")

    @property
    def time(self):
        return self.datetime.strftime("%H:%M")
