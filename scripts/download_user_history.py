import pickle
import pandas as pd

from scrapers.userdata import UserDataScraper
from utils.data_converter import DataConverter
from tqdm import tqdm


def main():
    print('Downloading history...')
    users_histories = pd.DataFrame()
    with open('../data/usernames.pkl', 'rb') as file:
        usernames = pickle.load(file)
        for username in tqdm(usernames):
            data = UserDataScraper(username).get_data()
            data = DataConverter(data).get_data()
            data['username'] = username
            users_histories = users_histories.append(data)
    print('Saving history...')
    with open('../data/users_histories.pkl', 'wb') as file:
        pickle.dump(users_histories, file)


if __name__ == '__main__':
    main()
