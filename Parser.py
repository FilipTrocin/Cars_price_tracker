import requests
import bs4

s = requests.Session()


def get_connection(mode, link, file_name):
    """
    :param file_name:
    :param mode: mode for which you want to make a request
    :param link: link to the website you request to get content
    :return: established connection
    """
    with open(file_name, 'w') as file:
        agent = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}
        req = s.request(mode, link, stream=True, headers=agent)
        cont = req.text
        file.write(cont)


connection = get_connection('GET', 'https://www.otomoto.pl/osobowe/suzuki/samurai/', "index.html")
file = 'index.html'

soup = bs4.BeautifulSoup(open(file), 'html.parser')


def get_year():
    car_year = []
    div = soup.find_all('li', {'data-code': 'year'}, limit=None)
    for index, item in enumerate(div):
        year = item.find('span')
        content = year.contents
        processed = ''.join([x.strip() for x in content])
        car_year.append(int(processed))
    return car_year


def get_mileage():
    mileage = []
    div = soup.find_all('li', {'data-code': 'mileage'}, limit=None)
    for index, item in enumerate(div):
        year = item.find('span')
        content = year.contents
        processed = ''.join([x.replace(' ', '') for x in content]).replace('km', '')
        mileage.append(int(processed))
    return mileage


print(get_mileage())
print(get_year())

s.close()
