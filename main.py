import logging
from scrape import scrape


if __name__ == "__main__":
    logging.basicConfig(filename='main.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started')
    url = "https://theverge.com"
    obj = scrape(url)
    obj.scraping()
    logging.info('Ended')
