import csv


class csvprocess:
    def __init__(self, fname: str) -> None:
        self.__fname = fname+'.csv'

    def listdicttocsv(self, data: list):
        keys = data[0].keys()
        with open(self.__fname, 'w', newline='') as opf:
            dwriter = csv.DictWriter(opf, keys)
            dwriter.writeheader()
            dwriter.writerows(data)
