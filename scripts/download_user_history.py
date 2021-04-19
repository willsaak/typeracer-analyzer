import pickle
import pandas as pd

from scrapers.userdata import UserDataScraper
from utils.data_converter import DataConverter
from tqdm import tqdm


def download_user_histories():
    print('Downloading history...')
    with open('../data/usernames.pkl', 'rb') as file:
        usernames = pickle.load(file)
    for username in tqdm(usernames):
        data = UserDataScraper(username).get_data()
        data = DataConverter(data).get_data()
        data['username'] = username
        with open(f'../data/user_histories/{username}_history.pkl', 'wb') as file:
            pickle.dump(data, file)


def combine_user_histories():
    print('Combining histories...')


def main():
    download_user_histories()
    combine_user_histories()


if __name__ == '__main__':
    main()
