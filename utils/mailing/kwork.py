import requests
from requests import Response

from bs4 import BeautifulSoup

DATA = {
    'Создание сайтов': '37',
    '10000': {
        'from': '10000',
        'to': '50000'
    }
}


class KWorkParser:
    """Парсинг с сайта kwork.ru"""

    def __init__(self, category, cost):
        self.url = f'https://kwork.ru/projects?c={DATA[f"{category}"]}&price-from={DATA[f"{cost}"]["from"]}&price-to={DATA[f"{str(cost)}"]["to"]}'
        self.HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
        self.data = []

    def get_html(self, params=None) -> Response:
        """Получение html кода"""

        response = requests.get(url=self.url, headers=self.HEADERS, params=params)
        response.encoding = 'utf-8'
        return response

    def get_content(self, html) -> list:
        """Получение нужного контента"""

        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='card')
        for item in items:
            self.data.append(
                {
                    'title': item.find(name='div', class_='wants-card__header-title').find('a').string,
                    'link': item.find(name='div', class_='wants-card__header-title').find('a').get('href'),
                    'description': item.find(
                        name='div', class_='wants-card__description-text'
                    ).text.replace('\r', ' ').replace('\n', ' ').replace('\xa0', '').replace('\t', ' ').replace('...', ' '),
                    'price': item.find(name='div', class_='m-visible').text.replace('\xa0', '').replace('Д', ' Д')
                }
            )
        return self.data

    def parse(self) -> list or str:
        html = self.get_html()
        if html.status_code == 200:
            return self.get_content(html=html.text)
        return 'error'
