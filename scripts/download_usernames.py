import pickle

from scrapers.username import UsernameScraper


def main():
    print('Extracting usernames...')
    usernames = UsernameScraper().get_data()
    print('Saving usernames...')
    with open('../data/usernames.pkl', 'wb') as file:
        pickle.dump(usernames, file)


if __name__ == '__main__':
    main()
