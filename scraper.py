from driver import ChromeDriver


class Scraper:
    def __init__(self, username):
        self._username = username
        self._driver = ChromeDriver().get()

    def get_data(self):
        url = f'https://data.typeracer.com/pit/race_history?user={self._username}&n=100000&startDate='
        content = self._driver.get(url)
        table = self._driver.find_element_by_class_name('scoresTable')
        trs = table.find_elements_by_tag_name('tr')
        ths = trs[0].find_elements_by_tag_name('th')
        column_names = [th.text for th in ths[:-1]]

        all_values = []
        for tr in trs[1:]:
            tds = tr.find_elements_by_tag_name('td')
            values = []
            for td in tds[:-1]:
                values.append(td.text)
            all_values.append(values)

        return all_values, column_names
