from scraper import Scraper
from data_converter import DataConverter


def main():
    extracted_data = Scraper(username='username').get_data()
    converter = DataConverter(*extracted_data)
    preprocessed_data = converter.get_data()
    converter.plot()


if __name__ == "__main__":
    main()
