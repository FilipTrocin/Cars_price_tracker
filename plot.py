import matplotlib.pyplot as plt
from calculations import days_sorted, boundaries, daily_prices, avg_weekly_price
from matplotlib.ticker import FormatStrFormatter
from kivy.properties import StringProperty
from os import listdir, remove, path

bar_width = 0.65
day_bars = 7
week_bars = 4


def delete_graphs():
    for file in listdir():
        if file.startswith('daily') or file.startswith('weekly'):
            remove(path=path.join(path.dirname(__file__), file))


delete_graphs()


def put_some_numbers(values, sep_num):
    """
    Method making 2d lists both for dates as well as prices, where each internal one has 10 elements
    :param values: dates or prices
    :param sep_num: number of dates/prices in an inside list
    :return: 2d lists of dates and prices
    """
    segregated = []
    count = 0
    temp = []
    for num, index in enumerate(values):
        if count < sep_num:
            temp.append(index)
            count += 1
        else:
            cp = temp.copy()
            segregated.append(cp)
            temp.clear()
            count = 0
        if num % sep_num == 0 and num != 0:
            temp.append(index)
            count += 1
        if num == len(values) - 1:
            if count == 0:
                temp.append(index)
                count += 1
            cp = temp.copy()
            segregated.append(cp)
            temp.clear()

    return segregated


def create_indexes(values, sep_num, initial_k, general_k):
    """
    Method creating unique indexes for every 10 elements
    :param initial_k: name of the first key
    :param general_k: general rule naming for the following keys
    :param values: values to create indexes for
    :param sep_num: how many dates/prices be on one index
    :return: lists of keys both for dates and prices
    """
    cnt = 0
    keys_c = 1
    keys = []
    for _ in values:
        if not keys:
            keys.append(initial_k)
        if cnt == sep_num:
            keys.append(f'{general_k}{keys_c}')
            keys_c += 1
            cnt = 0
        else:
            cnt += 1

    return keys


def create_dictionaries(dates, prices, sep_num):
    """
    Method creating a dictionary of keys (products of create_index method) and values
    (products of add_ten_dates method)
    :return: dict of dates and prices
    """
    dt_dictionary = dict()
    pr_dictionary = dict()

    count = 0

    dt_lst = put_some_numbers(dates, sep_num)
    pr_lst = put_some_numbers(prices, sep_num)

    dt_keys = create_indexes(dates, sep_num, 'data0', 'data')
    pr_keys = create_indexes(prices, sep_num, 'price0', 'price')

    for key in dt_keys:
        dt_dictionary[key] = dt_lst[count]
        count += 1

    count = 0
    for key in pr_keys:
        pr_dictionary[key] = pr_lst[count]
        count += 1

    return dt_dictionary, pr_dictionary


def create_namings(dates, prices, f_name, sep_num):
    dictionary = dict()
    for data in range(len(graph_input(dates, prices, sep_num)[0])):
        name = f'{f_name}{data}'
        dictionary[name] = StringProperty('./{}.png'.format(name))
    return dictionary


def graph_input(dates, prices, sep_num):
    dt_dictionary, pr_dictionary = create_dictionaries(dates, prices, sep_num)

    dt_keys = [x for x in dt_dictionary.keys()]
    pr_keys = [x for x in pr_dictionary.keys()]

    all_dates = []  # 2D list of lists with dates
    for num in range(len(dt_keys)):
        all_dates.append(dt_dictionary.get(dt_keys[num]))
    # print(all_dates)

    all_prices = []  # 2D list of lists with prices
    for num in range(len(pr_keys)):
        all_prices.append(pr_dictionary.get(pr_keys[num]))
    # print(all_prices)

    return all_dates, all_prices


def plot_daily_graph():
    all_dates, all_prices = graph_input(days_sorted, daily_prices, day_bars)

    num = 0
    for dates in all_dates:
        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(10, 4))

        formatter = FormatStrFormatter('%1.2f PLN')
        ax.yaxis.set_major_formatter(formatter)

        rectangle = ax.bar(all_dates[num], all_prices[num], bar_width, color='darkorange')
        up_label(ax, rectangle)

        plt.savefig(list(create_namings(days_sorted, daily_prices, 'daily', day_bars))[num], bbox_inches='tight')
        plt.show()
        if dates != all_dates[-1]:
            num += 1


def plot_weekly_graph():
    all_dates, all_prices = graph_input(boundaries, avg_weekly_price, week_bars)

    num = 0
    for dates in all_dates:
        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(10, 4))

        formatter = FormatStrFormatter('%1.2f PLN')
        ax.yaxis.set_major_formatter(formatter)

        rectangle = ax.bar(all_dates[num], all_prices[num], bar_width, color='midnightblue')
        up_label(ax, rectangle)

        plt.savefig(list(create_namings(boundaries, avg_weekly_price, 'weekly', week_bars))[num], bbox_inches='tight')
        plt.show()
        if dates != all_dates[-1]:
            num += 1


def up_label(axis, rect):
    """
    Method placing exact price above each bar
    :param axis: axis with values to be placed
    :param rect: bar above which the values be placed
    :return:
    """
    for bar in rect:
        height = bar.get_height()
        axis.annotate(f'{height} PLN', xy=(bar.get_x() + bar.get_width() / 2, height),
                      xytext=(0, 1), textcoords='offset points', ha='center', va='bottom')