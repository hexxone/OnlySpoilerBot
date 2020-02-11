import re
from collections import deque

import requests

from bot.weekdays import WeekInfo, DayInfo, HourInfo

locations = {
    'fitx_adenauer': 'https://www.google.de/maps/place/FitX+Fitnessstudio/@51.5495502,7.0786878,' \
                     '17z/data=!3m1!4b1!4m5!3m4!1s0x47b8e7053e64b21b:0xaf67314083f991e8!8m2!3d51.5495502!4d7.0808765'
                     '?hl=de',
    'fitx_asbeck': 'https://www.google.de/maps/place/FitX+Fitnessstudio/@51.523014,7.0663099,' \
                   '15.5z/data=!4m5!3m4!1s0x47b8e645c7f82f75:0x4338a1e7f7deee66!8m2!3d51.5237398!4d7.071133?hl=de' \
                   '&authuser=0',
    'sug_buer': 'https://www.google.de/maps/place/Sport-+und+Gesundheitszentrum+Buer/@51.5800968,7.0451868,'
                '14z/data=!4m5!3m4!1s0x0:0xd1508f85ba1da6b5!8m2!3d51.5830099!4d7.0427299?hl=de '
}


def get_html(location):
    """Takes a url and returns the html-get-response as utf-8 string"""
    url = locations[location]
    ret = requests.get(url, {}).text
    # with open('maps_data.txt', 'r+', encoding='utf-8') as file:
    #     file.write(ret)
    return ret


def extract_week(maps_html):
    pattern = r'\[[0-9]{1,3},[0-9]{1,3},[^\]]+\"\]'
    hours_tokens = re.findall(pattern, maps_html)

    # weeks in gmaps start with Sunday, 04:00 -> convert to deque and rotate
    # note: positive values rotate right (backwards) and negative values rotate left (forwards)
    hours_deque = deque(hours_tokens)
    hours_deque.rotate(4 - 24)

    # extract hours
    hours_extracted = []
    for hour in hours_deque:
        # turn unformatted string into usable information
        hour_extracted = re.findall(r'[\w\s]+', hour)

        # extracted data now in the current form: [time, crowded, ...]
        time, crowded = [hour_extracted[i] for i in (0, 1)]
        hours_extracted.append(HourInfo(time, crowded))

    # add hours to weekdays and put in weekday object
    week = WeekInfo()
    for day_index in range(7):
        day = DayInfo(day_index)
        for hour_index in range(24):
            day.add_hour(hours_extracted[day_index * 24 + hour_index])
        week.add_day(day)

    return week


def extract_current_hour(maps_html):
    pattern = r'\\\"[^\]]+\\\",\[[0-9]{1,3},[0-9]{1,3}\]'
    current_day_token = re.findall(pattern, maps_html)[0]  # get token from html
    extracted_data = re.findall(r'[\w\s]+', current_day_token)  # extract usable data

    # extracted data now in the current form: [info text, time, crowded] OR [time, crowded]
    if len(extracted_data) == 2:
        time, crowded = [extracted_data[i] for i in (0, 1)]
    else:
        time, crowded = [extracted_data[i] for i in (1, 2)]

    return HourInfo(int(time), crowded)
