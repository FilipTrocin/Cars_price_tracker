import matplotlib.pyplot as plt
from calculations import dates_present, boundaries, avg_daily_price, avg_weekly_price
from matplotlib.ticker import FormatStrFormatter


def add_ten_dates(dates, prices):
    """
    :param prices:
    :param dates: list of all dates to be segregated
    :return: list of lists of 10 dates inside each internal one or the remaining dates if there was no 10
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
            cp = temp_p.copy()
            ten_prices.append(cp)
            temp_p.clear()

    return ten_dates, ten_prices


def create_index(dates, prices):
    """
    Method creating unique indexes for every 10 elements
    :param prices:
    :param dates: list of dates
    :return: list of dates_keys
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


def create_dictionary(dates, prices):
    """
    Method creating a dictionary of keys (products of create_index method) and values
    (products of add_ten_dates method)
    :return:
    """
    dt_dictionary = dict()
    pr_dictionary = dict()
    count = 0
    dt_lst, pr_lst = add_ten_dates(dates, prices)
    dt_keys, pr_keys = create_index(dates, prices)

    for key in dt_keys:
        dt_dictionary[key] = dt_lst[count]
        count += 1

    count = 0
    for key in pr_keys:
        pr_dictionary[key] = pr_lst[count]
        count += 1

    return dt_dictionary, pr_dictionary


def plot_daily_graph():
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 4))

    formatter = FormatStrFormatter('%1.2f PLN')
    ax.yaxis.set_major_formatter(formatter)

    plt.bar(dates_present, avg_daily_price, color="orangered")
    plt.savefig('daily.png', bbox_inches='tight')


def plot_weekly_graph():
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 4))

    formatter = FormatStrFormatter('%1.2f PLN')
    ax.yaxis.set_major_formatter(formatter)

    plt.bar(boundaries, avg_weekly_price, color="turquoise")
    plt.savefig('weekly.png', bbox_inches='tight')
    plt.show()
