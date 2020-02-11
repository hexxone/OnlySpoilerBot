import re
from enum import Enum

Weekdays = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnrstag",
    "Freitag",
    "Samstag",
    "Sonntag"
]


class HourInfo:
    """data which can be assigned to one hour"""

    def __init__(self, time: int, crowded):
        self.time = time
        self.crowded = crowded

    def __str__(self):
        return "[" + str(self.time) + ", " + self.crowded + "]"


class DayInfo:
    """Encapsulates a list of HourInformation objects to represent a whole day"""

    def __init__(self, day_index):
        self.hours = []
        self.name = Weekdays[day_index]

    def __str__(self):
        ret = self.name + '\n'
        for hour in self.hours:
            ret += str(hour) + '\n'
        return ret

    def set_hour(self, hour_index: int, info: HourInfo):
        self.hours[hour_index] = info

    def add_hour(self, info: HourInfo):
        self.hours.append(info)

    def get_hour(self, hour: int):
        return self.hours[hour]


class WeekInfo:
    """Encapsulates a list of DayInformation objects to represent a whole Week"""

    def __init__(self):
        self.days = []

    def __str__(self):
        ret = ''
        for day in self.days:
            ret += str(day) + '\n'
        return ret

    def set_day(self, day_index: int, info: DayInfo):
        self.days[day_index] = info

    def add_day(self, info: DayInfo):
        self.days.append(info)

    def get_day(self, weekday_index):
        return self.days[weekday_index]
