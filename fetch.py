import logging
import requests


class fetch:
    """
    class to fetch data from a url using requests package
    """

    def __init__(self, url: str) -> None:
        """initialise

        Args:
            url (str): url from where the data is to be fetched
        """
        self.__url = url

    def get(self) -> requests:
        """fetch content from url

        Returns:
            requests: request object of get request
        """
        r = requests.get(self.__url)
        logging.info('satus code for get request on %s : %s',
                     self.__url, r.status_code)
        return r
