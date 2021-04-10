from utils.driver import ChromeDriver
from tqdm import tqdm


class UsernameScraper:
    def __init__(self):
        self._driver = ChromeDriver().get()

    def get_data(self):
        url = 'http://typeracerdata.com/leaders?min_races=1000&min_texts=400&sort=wpm_textbests&rank_start=1&rank_end=20000'
        content = self._driver.get(url)
        table = self._driver.find_element_by_class_name('stats')
        trs = table.find_elements_by_tag_name('tr')

        usernames = []
        for tr in tqdm(trs[1:]):
            link = tr.find_element_by_class_name('l').find_element_by_tag_name('a').get_attribute('href')
            username = link[link.rfind('=') + 1:]
            usernames.append(username)

        return usernames
