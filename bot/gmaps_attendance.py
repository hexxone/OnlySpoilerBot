import re
import requests

from bot.attendance_information import HourInformation


def extract_week(maps_html):
    pattern = r'\[[0-9]{1,3},[0-9]{1,3},[^\]]+\"\]'


def extract_current_hour(maps_html):
    pattern = r'\\\"[^\]]+\\\",\[[0-9]{1,3},[0-9]{1,3}\]'
    current_day_token = re.findall(pattern, maps_html)[0]  # get token from html
    extracted_data = re.findall(r'[\w\s]+', current_day_token)  # extract usable data

    # extracted data now in the current form: [info text, time, crowded]
    info_text, time, crowded = extracted_data
    return HourInformation(time, crowded, info_text)
