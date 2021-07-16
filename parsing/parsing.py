import requests
from bs4 import BeautifulSoup

class Parsing:
    
    def __init__(self, url, url_1):
        self.url = url
        self.url_1 = url_1
        self.info = []
        self.currency = []
        source = requests.get(self.url)
        source_1 = requests.get(self.url_1)
        self.html = BeautifulSoup(source.text, 'lxml')
        self.html_1 = BeautifulSoup(source_1.text, 'lxml')

    def get_info(self):
        table = self.html.find('table', {'class': 'content_table with_department head_2_row'})
        tbody = table.find('tbody')
        for tr in tbody.find_all('tr'):
            for div in tr.find_all('div', {'class': 'bank_name__content'}):
                a = div.get_text().strip()
                self.info.append(a)
            
            for td in tr.find_all('td', {'class': 'curr_hid USD'}):
                for value in td:
                    self.info.append(value)

            for td in tr.find_all('td', {'class': 'best curr_hid USD'}):
                for value in td:
                    self.info.append(value)

            for td in tr.find_all('td', {'class': 'curr_hid EUR'}):
                for value in td:
                    self.info.append(value)

            for td in tr.find_all('td', {'class': 'best curr_hid EUR'}):
                for value in td:
                    self.info.append(value)
                    
        table_1 = self.html_1.find('table', {'class': 'data'})
        tbody = table_1.find('tbody')
        for tr in tbody.find_all('tr'):
            for td in tr.find_all('td'):
                for value in td:
                    self.currency.append(value)
        
        del self.currency[::5]
        del self.currency[::4]

        return self.info