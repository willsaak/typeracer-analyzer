from scrapers.userdata import UserDataScraper
from utils.data_converter import DataConverter


def main():
    print('Getting data...')
    extracted_data = UserDataScraper(username='hinkalus').get_data()
    print('Converting to pandas df...')
    converter = DataConverter(*extracted_data)
    preprocessed_data = converter.get_data()
    print('Plotting...')
    converter.plot()


if __name__ == "__main__":
    main()
