import requests
import bs4
import datetime
from UI import user_input
s = requests.Session()

today = '{dt.year}-{dt.month}-{dt.day}'.format(dt=datetime.datetime.now())
web_results = []


def get_connection(mode, file_name, made, model):
    """
    :param file_name:
    :param mode: mode for which you want to make a request
    :param link: link to the website you request to get content
    :return: established connection
    """
    with open(file_name, 'w') as file:
        website = 'https://www.otomoto.pl/osobowe/{}/{}/'
        agent = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}
        req = s.request(mode, website.format(made, model), stream=True, headers=agent)
        cont = req.text
        file.write(cont)


def parse_html(made, model):
    get_connection('GET', 'index.html', made, model)
    file = 'index.html'
    return bs4.BeautifulSoup(open(file), 'html.parser')


# Here I can swap 'suzuki' and 'samurai' by any other car make and model. User will be able to decide
soup = parse_html(user_input[0], user_input[1])


def get_make():
    """
    :return: list with car makes of all cars
    """
    car_make = []
    h2 = soup.find_all('h2', {'class': 'offer-title ds-title'}, limit=None)
    for index, item in enumerate(h2):
        make = item.find('a')
        content = make.contents
        processed = ''.join([x.strip() for x in content])
        splitted = processed.lower().split()
        car_make.append(splitted[0])
    return car_make


def get_model():
    """
    :return: list with car models of all cars
    """
    car_model = []
    h2 = soup.find_all('h2', {'class': 'offer-title ds-title'}, limit=None)
    for index, item in enumerate(h2):
        make = item.find('a')
        content = make.contents
        processed = ''.join([x.strip() for x in content])
        splitted = processed.lower().split()
        car_model.append(splitted[1])
    return car_model


def get_year():
    """
    :return: list with car years of all cars
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
    :return: list with type of fuel of all cars - 'Benzyna' or 'Diesel' or 'Benzyna+LPG'
    """
    car_fuel_type = []
    div = soup.find_all('li', {'data-code': 'fuel_type'}, limit=None)
    for index, item in enumerate(div):
        fuel_type = item.find('span')
        content = fuel_type.contents
        processed = ''.join([x.replace(' ', '') for x in content])
        car_fuel_type.append(processed.lower())
    return car_fuel_type


def get_price():
    """
    :return: list with price of all cars
    """
    car_price = []
    div = soup.find_all('div', {'class': 'price-wrapper-listing'}, limit=None)
    for index, item in enumerate(div):
        fuel_type = item.find('span')
        content = fuel_type.contents
        processed = ''.join([x.replace(' ', '') for x in content[1]])
        if "," in processed:
            processed = processed.split(",", 1)[0]
        car_price.append(int(processed))
    return car_price


def create_car_object():
    """
    Method producing CarObject instances by reading particular parameters from 'get' methods
    :return:
    """
    global web_results
    for index in range(len(get_year())):
        web_results.append(CarObject(get_make()[index], get_model()[index], get_mileage()[index], get_year()[index],
                                     get_engine_capacity()[index],
                                     get_fuel_type()[index], get_price()[index], today))


def create_entry():
    """
    Method printing all of the CarObject instances in a particular template
    :return:
    """
    cars_lst = []
    global web_results
    for index in range(0, len(web_results)):
        cars_lst.extend(web_results[index].entry_model())
    return cars_lst


class CarObject(object):
    def __init__(self, make, model, mileage, year, engine, engine_type, price, searches):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.year = year
        self.engine = engine
        self.fuel_type = engine_type
        self.price = price
        self.searches = searches

    def entry_model(self):
        """
        Method declaring format in which CarObject instances data be send to MongoDB database
        :return: list with specified format
        """
        entry_format = [{'MAKE': self.make, 'MODEL': self.model, 'MILEAGE': self.mileage, 'YEAR': self.year,
                         'ENGINE': self.engine, 'ENGINE_TYPE': self.fuel_type, 'PRICE': self.price,
                         'SEARCHES': self.searches}]

        return entry_format


def create_entry_sender(child_conn):
    """
    Function initialising create_entry method and sending it's results to
    :param child_conn: results of create_entry method to be send
    :return:
    """
    results = create_entry()
    child_conn.send(results)
    child_conn.close()


create_car_object()
s.close()
