import urllib.request
import json


class UserDataScraper:
    def __init__(self, username):
        self._username = username

    def get_data(self):
        url = f'https://data.typeracer.com/games?playerId=tr:{self._username}&universe=play&startDate=1095166400&endDate=2495252800'
        with urllib.request.urlopen(url) as url_data:
            data = json.loads(url_data.read().decode())

        return data
