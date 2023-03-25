from datetime import datetime
import logging
from csvprocess import csvprocess
from database import database
from scrape import scrape


if __name__ == "__main__":
    logging.basicConfig(filename='main.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started')

    url = "https://theverge.com"
    date = datetime.now().strftime('%Y%m%d')
    dbname = 'vergedatabase'
    fname = date+"_verge"

    dobj = database(dbname)

    i = dobj.getkeyindex()
    if i == None:
        i = -1
    i = i + 1

    scrapeobj = scrape(url)
    details = scrapeobj.scraping(i, 10)

    dobj.insert(details)

    cobj = csvprocess(fname)
    cobj.listdicttocsv(details)

    dobj.close()

    logging.info('Ended')
