import requests
import io


def get_html(url):
    """Takes a url and returns the html-get-response as utf-8 string"""
    ret = requests.get(url, {}).text
    with open('maps_data.txt', 'r+', encoding='utf-8') as file:
        file.write(ret)
    return ret

