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
        agent = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}
        req = s.request(mode, link, stream=True, headers=agent)
        cont = req.text
        file.write(cont)

# Here I can swap 'suzuki' and 'samurai' by any other car make and model. User will be able to decide
connection = get_connection('GET', 'https://www.otomoto.pl/osobowe/suzuki/samurai/', "index.html")
file = 'index.html'

soup = bs4.BeautifulSoup(open(file), 'html.parser')


def get_year():
    """
    :return: list with car years made of all cars
    """
    car_year = []
    div = soup.find_all('li', {'data-code': 'year'}, limit=None)
    for index, item in enumerate(div):
        year = item.find('span')
        content = year.contents
        processed = ''.join([x.strip() for x in content])
        car_year.append(int(processed))
    return car_year


def get_mileage():
    """
    :return: list with mileage of all cars
    """
    car_mileage = []
    div = soup.find_all('li', {'data-code': 'mileage'}, limit=None)
    for index, item in enumerate(div):
        mileage = item.find('span')
        content = mileage.contents
        processed = ''.join([x.replace(' ', '') for x in content]).replace('km', '')
        car_mileage.append(int(processed))
    return car_mileage


def get_engine_capacity():
    """
    :return: list of engine capacities of all cars. If user did not specify it, then it assigns 0 to that position
    """
    car_engine_capacity = []
    params_block = soup.find_all('ul', {'class': 'ds-params-block'}, limit=None)
    for li in params_block:
        dt_exist = li.find('li', {'data-code': 'engine_capacity'})
        if dt_exist:
            engine_capacity = dt_exist.find('span')
            content = engine_capacity.contents
            processed = ''.join([x.replace(' ', '') for x in content]).replace('cm3', '')
            car_engine_capacity.append(int(processed))
        else:
            car_engine_capacity.append(0)

    return car_engine_capacity


def get_fuel_type():
    """
    :return: list with type of fuel of all cars
    """
    car_fuel_type = []
    div = soup.find_all('li', {'data-code': 'fuel_type'}, limit=None)
    for index, item in enumerate(div):
        fuel_type = item.find('span')
        content = fuel_type.contents
        processed = ''.join([x.replace(' ', '') for x in content])
        car_fuel_type.append(processed)
    return car_fuel_type


class Object():
    def __init__(self, make, model, mileage, year, engine, engine_type):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.year = year
        self.engine = engine
        self.engine_type = engine_type

    def create_object(self):
        """
        Method producing objects - matching all of the parameters together, producing key-value object which can be inserted
        into MongoDB database
        :return:
        """
        entry = [{'MAKE': self.make, 'MODEL': self.model, 'MILEAGE': self.mileage, 'YEAR': self.year,
                  'ENGINE': self.engine, 'ENGINE_TYPE': self.engine_type}]

        return entry


o1 = Object('suzuki', 'samurai', 91000, 1997, 1900, 'Benzyna')
print(o1.create_object())

print(get_mileage())
print(get_year())
print(get_engine_capacity())
print(get_fuel_type())


s.close()
