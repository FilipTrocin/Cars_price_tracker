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

connection = get_connection('GET', 'https://suchen.mobile.de/fahrzeuge/search.html?dam=0&isSearchRequest=true&ms=23600;17&sfmr=false&vc=Car', "index.html" )
file = 'index.html'


soup = bs4.BeautifulSoup(open(file), 'html.parser')
print(soup)

s.close()