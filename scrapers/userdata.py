import urllib.request
import urllib.error
import json


class UserDataScraper:
    def __init__(self, username):
        self._username = username

    def get_data(self):
        all_data = []
        start_date = '1000000000'
        end_date = '2000000000'
        while True:
            url = f'https://data.typeracer.com/games?playerId=tr:{self._username}&universe=play&startDate={start_date}&endDate={end_date}'
            try:
                with urllib.request.urlopen(url) as url_data:
                    data = json.loads(url_data.read().decode())
                    end_date = data[-1]['t'] - 0.01
                    all_data.extend(data)
            except urllib.error.HTTPError:
                break

        return all_data
