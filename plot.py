import matplotlib.pyplot as plt
from calculations import dates_present, boundaries, avg_daily_price, avg_weekly_price
from matplotlib.ticker import FormatStrFormatter
from kivy.properties import StringProperty
from os import listdir, remove, path


def delete_graphs():
    for file in listdir():
        if file.startswith('daily'):
            remove(path=path.join(path.dirname(__file__), file))


delete_graphs()


def add_ten(dates, prices):
    """
    Method making 2d lists both for dates as well as prices, where each internal one has 10 elements
    :param prices: list of all prices to be segregated
    :param dates: list of all dates to be segregated
    :return: 2d lists of dates and prices
    """
    ten_dates = []
    ten_prices = []
    count = 0
    temp_d = []
    temp_p = []
    for date in dates:
        if count < 10:
            temp_d.append(date)
            count += 1
        else:
            cp = temp_d.copy()
            ten_dates.append(cp)
            temp_d.clear()
            count = 0
        if date is dates[-1]:
            if count == 0:
                temp_d.append(date)  # TESTING PHASE
                count += 1
            cp = temp_d.copy()
            ten_dates.append(cp)
            temp_d.clear()

    count = 0
    for price in prices:
        if count < 10:
            temp_p.append(price)
            count += 1
        else:
            cp = temp_p.copy()
            ten_prices.append(cp)
            temp_p.clear()
            count = 0
        if price is prices[-1]:
            if count == 0:
                temp_p.append(price)  # TESTING PHASE
                count += 1
            cp = temp_p.copy()
            ten_prices.append(cp)
            temp_p.clear()
    return ten_dates, ten_prices


def create_indexes(dates, prices):
    """
    Method creating unique indexes for every 10 elements
    :param prices: list of prices
    :param dates: list of dates
    :return: lists of keys both for dates and prices
    """
    cnt = 0
    keys_c = 1
    dates_keys = []
    for _ in dates:
        if not dates_keys:
            dates_keys.append('data0')
        if cnt == 10:
            dates_keys.append('data{}'.format(keys_c))
            keys_c += 1
            cnt = 0
        else:
            cnt += 1

    cnt = 0
    keys_c = 1
    prices_keys = []
    for _ in prices:
        if not prices_keys:
            prices_keys.append('price0')
        if cnt == 10:
            prices_keys.append('price{}'.format(keys_c))
            keys_c += 1
            cnt = 0
        else:
            cnt += 1
    return dates_keys, prices_keys


def create_dictionaries(dates, prices):
    """
    Method creating a dictionary of keys (products of create_index method) and values
    (products of add_ten_dates method)
    :return: dict of dates and prices
    """
    dt_dictionary = dict()
    pr_dictionary = dict()
    count = 0
    dt_lst, pr_lst = add_ten(dates, prices)
    dt_keys, pr_keys = create_indexes(dates, prices)

    for key in dt_keys:
        dt_dictionary[key] = dt_lst[count]
        count += 1

    count = 0
    for key in pr_keys:
        pr_dictionary[key] = pr_lst[count]
        count += 1

    return dt_dictionary, pr_dictionary


def create_namings():
    dictionary = dict()
    for data in range(len(graph_input()[0])):
        name = 'daily{}'.format(data)
        dictionary[name] = StringProperty('./{}.png'.format(name))
    return dictionary


def graph_input():
    dt_dictionary, pr_dictionary = create_dictionaries(dates_present, avg_daily_price)

    dt_keys = [x for x in dt_dictionary.keys()]
    pr_keys = [x for x in pr_dictionary.keys()]

    all_dates = []  # 2D list of lists with 10 dates
    for num in range(len(dt_keys)):
        all_dates.append(dt_dictionary.get(dt_keys[num]))
    # print(all_dates)

    all_prices = []  # 2D list of lists with 10 prices
    for num in range(len(pr_keys)):
        all_prices.append(pr_dictionary.get(pr_keys[num]))
    # print(all_prices)

    return all_dates, all_prices


def plot_daily_graph():
    all_dates, all_prices = graph_input()

    num = 0
    for dates in all_dates:
        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(10, 4))

        formatter = FormatStrFormatter('%1.2f PLN')
        ax.yaxis.set_major_formatter(formatter)

        plt.bar(all_dates[num], all_prices[num], color="orangered")
        plt.savefig(list(create_namings())[num], bbox_inches='tight')
        plt.show()
        if dates != all_dates[-1]:
            num += 1


def plot_weekly_graph():
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 4))

    formatter = FormatStrFormatter('%1.2f PLN')
    ax.yaxis.set_major_formatter(formatter)

    plt.bar(boundaries, avg_weekly_price, color="turquoise")
    plt.savefig('weekly.png', bbox_inches='tight')
    plt.show()
