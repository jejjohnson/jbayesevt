from dataclasses import dataclass
import datetime
import pandas as pd
from dateutil.parser import parse

@dataclass
class Time:
    datetime: datetime.datetime

    @classmethod
    def from_explicit_units(cls, *args, **kwargs):
        time = datetime.datetime(*args, **kwargs)
        return cls(time)

    @classmethod
    def from_datetime_str(cls, time: str):
        time = pd.Timestamp(time).to_pydatetime()
        return Time(datetime=time)

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
