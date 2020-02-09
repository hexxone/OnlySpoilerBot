import re
import ast
from collections import deque

from bot.gmaps_api import get_html


class HourInformation:
    """data which can be assigned to one hour"""

    def __init__(self, time, crowded, info_text):
        self.time = time
        self.crowded = crowded
        self.info_text = info_text

    def __str__(self):
        return "[" + self.time + ", " + self.crowded + ", " + self.info_text + "]"

    def get_information(self):
        return 'zwischen ' + self.time + ' und ' + str(int(self.time)+1) + ' Uhr ist es ' + self.info_text + ', es ist zu ' + self.crowded + '% voll.'

    def get_information_current(self):
        return 'Jetzt gerade zwischen ' + self.time + ' und ' + str(int(self.time)+1) + ' Uhr ist es ' + self.info_text + ', es ist zu ' + self.crowded + '% voll.'

class DayInformation:
    """data which can be assigned to one day"""

    def __init__(self, hours_raw: list, name):
        self.hours = []
        self.orchestrate_data(hours_raw)
        self.name = name

    def __str__(self):
        ret = ''
        for hour in self.hours:
            ret += str(hour) + '\n'
        return ret

    def orchestrate_data(self, tokens):

        """expects a list of raw string tokens from """
        for token in tokens:
            token = re.sub(r'\\\"', '', token)
            token = re.sub(r',,', ',', token)
            information = re.findall(r'[\w\s]+', token)
            time = information[0]
            crowded = information[1]
            if len(information) == 4:
                info_text = information[2]
                info_time = information[3]
            else:
                info_text = 'Gar nicht besucht'
                info_time = information[2]
            current_hour = HourInformation(time, crowded, info_text, info_time)
            self.hours.append(current_hour)

    def get_hour(self, hour):
        return self.hours[hour]


class WeekInformation:

    def __init__(self):
        self.days = []

    def __str__(self):
        ret = ''
        for day in self.days:
            ret += str(day) + '\n'
        return ret

    def add(self, day: DayInformation):
        self.days.append(day)

    def get_day(self, weekday_index):
        return self.days[weekday_index]


class CrowdedInfo:
    """This class provides functions for accessing how crowded a place is on google maps via a generic google maps
    url """

    fitx_url = 'https://www.google.de/maps/place/FitX+Fitnessstudio/@51.5495502,7.0786878,' \
               '17z/data=!3m1!4b1!4m5!3m4!1s0x47b8e7053e64b21b:0xaf67314083f991e8!8m2!3d51.5495502!4d7.0808765?hl=de'

    weekdays = {
        'Montag': 0,
        'Dienstag': 1,
        'Mittwoch': 2,
        'Donnerstag': 3,
        'Freitag': 4,
        'Samstag': 5,
        'Sonntag': 6
    }

    def __init__(self):
        self.week = WeekInformation()
        self.raw_html = get_html(self.fitx_url)
        self.tokenize_weekdays()
        self.current_time = self.tokenize_current_hour()

    def tokenize_current_hour(self):
        current_pattern: str = r'\\\"[^\]]+\\\",\[[0-9]{1,3},[0-9]{1,3}\]'
        current_token: list = re.findall(current_pattern, self.raw_html)
        current_token: str = current_token[0]
        # current_token = re.sub(r'\\\"', '', current_token)
        information = re.findall(r'[\w\s]+', current_token)
        info_text = information[0]
        time = information[1]
        crowded = information[2]
        info_time = time + ':00 Uhr'
        return HourInformation(time, crowded, info_text, info_time)

    def tokenize_weekdays(self):
        # extract hours from raw html and put them into tokens
        hour_pattern: str = r'\[[0-9]{1,3},[0-9]{1,3},[^\]]+\"\]'  # finds an hour in a day
        hours_tokens: list = re.findall(hour_pattern, self.raw_html)

        # weeks start with Sunday, 04:00 -> Normalize to Monday 00:00
        # note: positive values rotate right (backwards) and negative values rotate left (forwards)
        hours_deque = deque(hours_tokens)
        hours_deque.rotate(4 - 24)

        iterator = 0  # too keep track of which hour we are at
        # put hour tokens into day objects and add them to week object
        # iterate over monday, tuesday, etc.
        for day in ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']:
            hours_raw = []
            for hour in range(24):
                current_hour_raw = hours_deque[iterator]
                hours_raw.append(current_hour_raw)
                iterator += 1
            self.week.add(DayInformation(hours_raw, day))

    def get_attendence(self, day, hour):
        day_index: int = self.weekdays[day]
        day: DayInformation = self.week.get_day(day_index)
        hour: HourInformation = day.get_hour(hour)
        return 'Am ' + day.name + ' ' + hour.get_information()

    def get_current_attendence(self):
        return self.current_time.get_information_current()



# simulate user input
# a = AttendanceInformation()
