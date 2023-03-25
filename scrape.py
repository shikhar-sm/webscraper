from datetime import datetime
import logging
from bs4 import BeautifulSoup
from csvprocess import csvprocess
from fetch import fetch


class scrape:
    """scrape verge
    """

    def __init__(self, url: str) -> None:
        """initialise

        Args:
            url (str): url for webpage
        """
        self.__url = url

    def __bsobjget(self, url, features='') -> BeautifulSoup:
        obj = fetch(url)
        res = obj.get()
        if res.status_code != 200:
            raise Exception('bad response')
        soup = BeautifulSoup(res.content, features=features)
        return soup

    def __processurlsoup(self, soupurl, i=0):
        details = {}

        # id
        details['id'] = i

        # url of article
        url = soupurl.find('loc').text
        details['url'] = url

        # headline for article
        headline = soupurl.find('news:title').text
        details['headline'] = headline

        # author
        bs = self.__bsobjget(url, features='html.parser')
        s = bs.find('span', attrs={
                    "class": "font-medium uppercase tracking-6"})
        author = s.a.text
        details['author'] = author

        # publication date
        date = soupurl.find('news:publication_date').text.split('T')[0]
        details['date'] = date

        logging.info("Gathering details %i is successful", i)

        return details

    def scraping(self):
        soup1 = self.__bsobjget(self.__url+'/sitemaps/google_news', 'xml')
        urls = soup1.find_all('url', limit=10)
        # print(urls)
        details = []
        for i, url in enumerate(urls):
            if url == None:
                continue
            logging.info('Processing article id: %i', i)
            details.append(self.__processurlsoup(url, i))
        fname = datetime.now().strftime('%Y%m%d')+"_verge"
        cobj = csvprocess(fname)
        cobj.listdicttocsv(details)
